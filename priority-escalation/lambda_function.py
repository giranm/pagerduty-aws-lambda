#!/usr/bin/env python3
import requests
import json

from config import pd_config, pd_api_headers
from logger import logger

# Main Lambda Entrypoint.


def lambda_handler(event, context):
    # Grab webhook payload and determine incidents in "triggered" state.
    messages = json.loads(event["body"])["messages"]
    for message in messages:
        if message["event"] == "incident.trigger":
            # Determine if priority is present and add escalation path.
            incident = message["incident"]
            if incident["priority"]:
                add_escalation_policy(incident)
            else:
                logger.warn(
                    "Triggered incident ({}) does not have priority - skipping".format(incident["id"]))

    return None

# Update incident escalation policy helper.


def add_escalation_policy(incident):

    # Define API params to update the incident.
    priority_summary = incident["priority"]["summary"]

    pd_incident_url = "{base}/incidents/{id}/responder_requests".format(
        base=pd_config["API_BASE_URL"], id=incident["id"])

    pd_additional_responder_payload = {
        "requester_id": get_api_user_id(),
        "message": "{} detected - please respond within SLA".format(priority_summary),
        "responder_request_targets": [
            {
                "responder_request_target": {
                    "id": get_ep_id(priority_summary),
                    "type": "escalation_policy"
                }
            }
        ]
    }

    # Update incident responders.
    logger.info("Adding {priority} escalation policy for incident: ({id}) {title}".format(
        priority=priority_summary, id=incident["id"], title=incident["title"]))

    pd_incident_update_response = requests.post(
        url=pd_incident_url,
        json=pd_additional_responder_payload,
        headers=pd_api_headers)

    if pd_incident_update_response.status_code == 200:
        logger.info("Incident successfully updated")
    else:
        logger.error("API failure while adding escalation policies")
        logger.error(pd_incident_update_response.json())

# Get current user id


def get_api_user_id():
    # This requests assumes there is only one user with the same email as provided in the config.
    logger.info("Getting User ID for {} to update incident responders".format(
        pd_config["API_USER"]))
    pd_user_response = requests.get(
        url="{base}/users?email={email}".format(
            base=pd_config["API_BASE_URL"], email=pd_config["API_USER"]),
        headers=pd_api_headers)
    return pd_user_response.json()["users"][0]["id"]

# Priority to escalation policy helper.


def get_ep_id(priority_summary):
    ep_ids = {
        "P1": pd_config["P1_EP_ID"],
        "P2": pd_config["P2_EP_ID"],
        "P3": pd_config["P3_EP_ID"],
        "P4": pd_config["P4_EP_ID"],
        "P5": pd_config["P5_EP_ID"]
    }
    return ep_ids.get(priority_summary, pd_config["DEFAULT_EP_ID"])

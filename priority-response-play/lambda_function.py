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
            # Determine if priority is present and trigger response play.
            incident = message["incident"]
            if incident["priority"]:
                trigger_response_play(incident)
            else:
                logger.warn(
                    "Triggered incident ({}) does not have priority - skipping".format(incident["id"]))

    return None

# Trigger response play helper.


def trigger_response_play(incident):

    # Check if response play id has been configured.
    priority_summary = incident["priority"]["summary"]
    response_play_id = get_rp_id(priority_summary)
    if response_play_id:
        # Prepare API call.
        pd_response_play_url = "{base}/response_plays/{response_play_id}/run".format(
            base=pd_config["API_BASE_URL"], response_play_id=response_play_id)

        pd_payload = {
            "incident": {
                "id": incident["id"],
                "type": "incident_reference"
            }
        }

        # Update incident responders.
        logger.info("Triggering {priority} response play for incident: ({id}) {title}".format(
            priority=priority_summary, id=incident["id"], title=incident["title"]))

        pd_incident_update_response = requests.post(
            url=pd_response_play_url,
            json=pd_payload,
            headers=pd_api_headers)

        if pd_incident_update_response.status_code == 200:
            logger.info("Incident successfully updated")
        else:
            logger.error("API failure while triggering response play")
            logger.error(pd_incident_update_response.json())
    else:
        logger.warn("Auto response play has not been configured for {} incidents - no further action taken".format(
            priority_summary))

# Priority to response play helper.


def get_rp_id(priority_summary):
    rp_ids = {
        "P1": pd_config["P1_RP_ID"],
        "P2": pd_config["P2_RP_ID"],
        "P3": pd_config["P3_RP_ID"],
        "P4": pd_config["P4_RP_ID"],
        "P5": pd_config["P5_RP_ID"]
    }
    return rp_ids.get(priority_summary, pd_config["DEFAULT_RP_ID"])

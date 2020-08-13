#!/usr/bin/env python3
import requests
import json

from config import pd_config
from logger import logger

# Main Lambda Entrypoint.


def lambda_handler(event, context):

    # Validate inputs.
    if "token" in event \
            and "auth_email" in event \
            and "alert_count" in event:

        # Prepare API call to obtain incidents.
        pd_api_headers = {
            "Authorization": "Token token={}".format(event["token"]),
            "Accept": "application/vnd.pagerduty+json;version=2",
            "Content-Type": "application/json",
            "From": event["auth_email"]
        }

        pd_incident_response = requests.get(
            url=pd_config["PD_INCIDENT_URL"],
            headers=pd_api_headers)

        # Iterate through open incidents and identify those with >= alert_count.
        if pd_incident_response.status_code == 200:
            incidents = pd_incident_response.json()["incidents"]

            if len(incidents) > 0:
                logger.info("Processing open incidents")
                for incident in incidents:
                    incident_id = incident["id"]
                    incident_alert_counts = incident["alert_counts"]["all"]

                    # If alert_count threshold is exceeded, grab alerts in current incident.
                    if incident_alert_counts >= event["alert_count"]:
                        alerts = get_alerts_from_incident(
                            incident_id, pd_api_headers)

                        # Determine the ideal priority state and if incident should be updated.
                        ideal_priority = get_priority_from_alerts(
                            alerts, pd_api_headers)
                        if incident["priority"]["summary"] != ideal_priority["summary"]:
                            update_incident_priority(
                                incident_id, ideal_priority, pd_api_headers)

                        else:
                            logger.info(
                                "Incident priority at ideal state - skipping")

                    # Current incident has alert_count below threshold.
                    else:
                        logger.warn("Incident {id} ({summary}) has {alert_counts} alert(s) - skipping".format(
                            id=incident_id,
                            summary=incident["summary"],
                            alert_counts=incident_alert_counts))
            else:
                logger.info("No open incidents - skipping")

        else:
            logger.error("Unable to retrieve incidents from API")

    else:
        logger.critical(
            "Missing config - please review inputs: {}".format(event))

    return None

# Get alerts from incident helper.


def get_alerts_from_incident(incident_id, pd_api_headers):
    pd_incident_alerts_url = "{base}/incidents/{id}/alerts".format(
        base=pd_config["API_BASE_URL"], id=incident_id)

    pd_incident_alerts_response = requests.get(
        url=pd_incident_alerts_url,
        headers=pd_api_headers)

    return pd_incident_alerts_response.json(
    )["alerts"] if pd_incident_alerts_response.status_code == 200 else []

# Determine ideal priority state from alerts helper.


def get_priority_from_alerts(alerts, pd_api_headers):

    # Use a default priority as as fallback.
    ideal_priority_summary = "P3"

    # Work through each alert and determine if any of the criticality matches - assign priority as needed.
    if any(alert['severity'] == 'critical' for alert in alerts):
        ideal_priority_summary = "P1"

    elif any(alert['severity'] != 'critical' and alert['severity'] == 'error' for alert in alerts):
        ideal_priority_summary = "P2"

    elif any(alert['severity'] != 'critical' and alert['severity'] != 'error' and alert['severity'] == 'warn' for alert in alerts):
        ideal_priority_summary = "P3"

    elif any(alert['severity'] != 'critical' and alert['severity'] != 'error' and alert['severity'] != 'warn' for alert in alerts):
        ideal_priority_summary = "P4"

    logger.info("Ideal priority for incident ({id}) should be {priority}".format(
        id=alerts[0]["incident"]["id"], priority=ideal_priority_summary))

    # Obtain priorities from domain and return ideal priority object.
    pd_priorities_response = requests.get(
        url=pd_config["PD_PRIORITY_URL"], headers=pd_api_headers)
    priorities = pd_priorities_response.json()["priorities"]

    return next(priority for priority in priorities if priority["summary"] == ideal_priority_summary)

# Update incident priority helper.


def update_incident_priority(incident_id, priority, pd_api_headers):
    logger.info("Updating incident priority")

    pd_incident_id_url = "{base}/incidents/{id}".format(
        base=pd_config["API_BASE_URL"],
        id=incident_id)

    pd_incident_payload = {
        "incident": {
            "type": "incident",
            "priority": priority
        }
    }

    pd_incident_update_response = requests.put(
        url=pd_incident_id_url,
        json=pd_incident_payload,
        headers=pd_api_headers)

    if pd_incident_update_response.status_code == 200:
        logger.info("Incident successfully updated")

    else:
        logger.error("Unable to update incident: {}".format(
            pd_incident_update_response.content))

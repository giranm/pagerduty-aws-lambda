#!/usr/bin/env python3
import requests

# Main Lambda Entrypoint.


def lambda_handler(event, context):

  # Define constants.
  PD_API_BASE = "https://api.pagerduty.com"
  PD_INCIDENT_URL = "{base}/incidents?{status}&{urgency}".format(
      base=PD_API_BASE,
      status="statuses[]=triggered&statuses[]=acknowledged",
      urgency="urgencies[]=low")

  # Validate inputs.
  response_dict = {}
  if "token" in event \
          and "auth_email" in event \
          and "alert_count" in event:

    # Define API headers.
    pd_headers = {
        "Authorization": "Token token={}".format(event["token"]),
        "Accept": "application/vnd.pagerduty+json;version=2",
        "Content-Type": "application/json",
        "From": event["auth_email"]
    }

    # Get open incidents which have low urgency set.
    pd_incident_response = requests.get(
        url=PD_INCIDENT_URL,
        headers=pd_headers)

    # Iterate through open incidents and identify those with >= alert_count.
    status_code = pd_incident_response.status_code
    if status_code == 200:
      incidents = pd_incident_response.json()["incidents"]

      if len(incidents) > 0:
        updated_incidents = []
        for incident in incidents:
          incident_id = incident["id"]
          incident_summary = incident["summary"]
          incident_alert_counts = incident["alert_counts"]["all"]

          # If alert_count threshold is exceeded, updated urgency of incident.
          if incident_alert_counts >= event["alert_count"]:
            print("Updating incident urgency to high: {id} | {summary} | Alerts: {alert_counts}".format(
                id=incident_id,
                summary=incident_summary,
                alert_counts=incident_alert_counts))

            pd_incident_id_url = "{base}/incidents/{id}".format(
                base=PD_API_BASE,
                id=incident_id)

            pd_incident_updated_payload = {
                "incident": {
                    "type": "incident",
                    "urgency": "high"
                }
            }

            pd_incident_update_response = requests.put(
                url=pd_incident_id_url,
                json=pd_incident_updated_payload,
                headers=pd_headers)

            # Validate if incident was successfully updated using API.
            if pd_incident_update_response.status_code == 200:
              print("Incident {} successfully updated".format(incident_id))
              updated_incidents.append(incident_id)

            elif pd_incident_update_response.status_code != 200:
              print("Unable to update incident: ",
                    pd_incident_update_response.content)

          # Current incident has alert_count below threshold.
          elif incident_alert_counts < event["alert_count"]:
            print("Low-urgency incident {id} ({summary}) has {alert_counts} alert(s) - skipping".format(
                id=incident_id,
                summary=incident_summary,
                alert_counts=incident_alert_counts))

        # Determine if any incidents have been updated and update response.
        if len(updated_incidents) > 0:
          response_dict = {
              "status_code": 200,
              "response_body": {
                  "updated_incidents": updated_incidents
              }
          }

        elif len(updated_incidents) == 0:
          response_dict = {
              "status_code": 204,
              "response_body": "No incidents updated"
          }

      # Zero low-urgency incidents.
      elif len(incidents) == 0:
        response_dict = {
            "status_code": 200,
            "response_body": "No open low-urgency incidents found",
        }

    # Error calling PagerDuty API (most likely failed auth)
    elif status_code != 200:
      response_dict = {
          "status_code": status_code,
          "response_body": {
              "error": "Unable to obtain incidents from PagerDuty API",
              "pd_api_response": pd_incident_response.content
          },
          "inputs": event
      }

  # Invalid inputs for Lambda.
  else:
    response_dict = {
        "status_code": 500,
        "response_body": "Invalid event structure - please review inputs",
        "inputs": event
    }

  # Response to client.
  print(response_dict)
  return response_dict

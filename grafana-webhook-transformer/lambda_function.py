#!/usr/bin/env python3
import requests
import json

# Main Lambda Entrypoint.


def lambda_handler(event, context):

  # Verify routing_key and severity as params.
  response = {}
  if "routing_key" in event["queryStringParameters"] \
          and "severity" in event["queryStringParameters"]:

    # Define PD API config.
    pd_event_api = "https://events.pagerduty.com/v2/enqueue"
    pd_headers = {
        "Content-Type": "application/json"
    }

    # Pass through alert into PagerDuty with some conformation to PD-CEF.
    grafana_alert = json.loads(event["body"])
    pd_event = {
        "event_action": "trigger",
        "client": "Grafana",
        "client_url": grafana_alert["ruleUrl"],
        "routing_key": event["queryStringParameters"]["routing_key"],
        "payload": {
            "summary": grafana_alert["title"],
            "severity": event["queryStringParameters"]["severity"],
            "source": "Grafana",
            "custom_details": grafana_alert
        },
        "images": [
            {
                "src": grafana_alert["imageUrl"],
                "href": grafana_alert["ruleUrl"],
                "alt": grafana_alert["title"]
            }
        ]
    }
    pd_event_response = requests.post(
        url=pd_event_api, headers=pd_headers, json=pd_event)

    # Update response based on PD API.
    response = {
        "status_code": pd_event_response.status_code,
        "response_body": json.dumps(pd_event_response.json())
    }

  # Update response if params are missing.
  else:
    response = {
        "status_code": 500,
        "response_body": "Parameter(s) missing from endpoint",
        "queryStringParameters": event["queryStringParameters"]
    }

  print(response)
  return response

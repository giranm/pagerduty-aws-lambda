#!/usr/bin/env python3

pd_config = {
    "API_BASE_URL": "https://api.pagerduty.com",
    "API_TOKEN": "<TOKEN>",
    "API_USER": "user@example.com",
    "P1_EP_ID": "<P1_ESCALATION_POLICY_ID>",
    "P2_EP_ID": "<P2_ESCALATION_POLICY_ID>",
    "P3_EP_ID": "<P3_ESCALATION_POLICY_ID>",
    "P4_EP_ID": "<P4_ESCALATION_POLICY_ID>",
    "P5_EP_ID": "<P5_ESCALATION_POLICY_ID>",
    "DEFAULT_EP_ID": "<DEFAULT_ESCALATION_POLICY_ID>"
}

pd_api_headers = {
    "Authorization": "Token token={}".format(pd_config["API_TOKEN"]),
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Content-Type": "application/json",
    "From": pd_config["API_USER"]
}

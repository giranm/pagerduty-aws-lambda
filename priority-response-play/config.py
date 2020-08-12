#!/usr/bin/env python3

pd_config = {
    "API_BASE_URL": "https://api.pagerduty.com",
    "API_TOKEN": "<TOKEN>",
    "API_USER": "user@example.com",
    "P1_RP_ID": "<P1_RESPONSE_PLAY_ID>",
    "P2_RP_ID": "<P2_RESPONSE_PLAY_ID>",
    "P3_RP_ID": None,
    "P4_RP_ID": None,
    "P5_RP_ID": None,
    "DEFAULT_RP_ID": None
}

pd_api_headers = {
    "Authorization": "Token token={}".format(pd_config["API_TOKEN"]),
    "Accept": "application/vnd.pagerduty+json;version=2",
    "Content-Type": "application/json",
    "From": pd_config["API_USER"]
}

#!/usr/bin/env python3
from lambda_function import lambda_handler

# Run Lambda function using test args through argv.
if __name__ == "__main__":
    args = {
        "version": "2.0",
        "routeKey": "ANY /echo-function",
        "rawPath": "/default/echo-function",
        "rawQueryString": "",
        "headers": {
            "accept": "application/json",
            "content-length": "5464",
            "content-type": "application/json",
            "host": "example_host.execute-api.us-east-1.amazonaws.com",
            "user-agent": "PagerDuty-Webhook/V2.0",
            "x-amzn-trace-id": "Root=1-5f32c2c1-59434981992f4c1c01605b28",
            "x-forwarded-for": "34.222.110.137",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https",
            "x-webhook-id": "0d5e7528-dbed-11ea-b3e3-0242c0a82a05"
        },
        "requestContext": {
            "accountId": "example_account_id",
            "apiId": "example_host",
            "domainName": "example_host.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "example_host",
            "http": {
                "method": "POST",
                "path": "/default/echo-function",
                "protocol": "HTTP/1.1",
                "sourceIp": "34.222.110.137",
                "userAgent": "PagerDuty-Webhook/V2.0"
            },
            "requestId": "RHNeLjD3oAMEVRQ=",
            "routeKey": "ANY /echo-function",
            "stage": "default",
            "time": "11/Aug/2020:16:09:37 +0000",
            "timeEpoch": 1597162177044
        },
        "body": "{\"messages\":[{\"event\":\"incident.trigger\",\"log_entries\":[{\"id\":\"R6O4ZYP1L0TW4JD129TE8KXT6C\",\"type\":\"trigger_log_entry\",\"summary\":\"Triggered through the website\",\"self\":\"https://api.pagerduty.com/log_entries/R6O4ZYP1L0TW4JD129TE8KXT6C\",\"html_url\":\"https://example_pd_domain.pagerduty.com/incidents/PKSEBO6/log_entries/R6O4ZYP1L0TW4JD129TE8KXT6C\",\"created_at\":\"2020-08-11T16:09:36Z\",\"agent\":{\"id\":\"PXNQ3VL\",\"type\":\"user_reference\",\"summary\":\"Giran Moodley\",\"self\":\"https://api.pagerduty.com/users/PXNQ3VL\",\"html_url\":\"https://example_pd_domain.pagerduty.com/users/PXNQ3VL\"},\"channel\":{\"type\":\"web_trigger\",\"summary\":\"P2 Incident\",\"subject\":\"P2 Incident\",\"details\":\"P2\",\"details_omitted\":false,\"body_omitted\":false},\"service\":{\"id\":\"PZDFEG1\",\"type\":\"service_reference\",\"summary\":\"TestService\",\"self\":\"https://api.pagerduty.com/services/PZDFEG1\",\"html_url\":\"https://example_pd_domain.pagerduty.com/service-directory/PZDFEG1\"},\"incident\":{\"id\":\"PKSEBO6\",\"type\":\"incident_reference\",\"summary\":\"[#154] P2 Incident\",\"self\":\"https://api.pagerduty.com/incidents/PKSEBO6\",\"html_url\":\"https://example_pd_domain.pagerduty.com/incidents/PKSEBO6\"},\"teams\":[],\"contexts\":[],\"event_details\":{\"description\":\"P2 Incident\"}}],\"webhook\":{\"endpoint_url\":\"https://example_host.execute-api.us-east-1.amazonaws.com/default/echo-function\",\"name\":\"Webhook\",\"description\":null,\"webhook_object\":{\"id\":\"PZDFEG1\",\"type\":\"service_reference\",\"summary\":\"TestService\",\"self\":\"https://api.pagerduty.com/services/PZDFEG1\",\"html_url\":\"https://example_pd_domain.pagerduty.com/service-directory/PZDFEG1\"},\"config\":{\"referer\":\"https://example_pd_domain.pagerduty.com/services/PZDFEG1/integrations?service_profile=1\"},\"outbound_integration\":{\"id\":\"PJFWPEP\",\"type\":\"outbound_integration_reference\",\"summary\":\"Generic V2 Webhook\",\"self\":\"https://api.pagerduty.com/outbound_integrations/PJFWPEP\",\"html_url\":null},\"accounts_addon\":null,\"id\":\"PVN3RMR\",\"type\":\"webhook\",\"summary\":\"Webhook\",\"self\":\"https://api.pagerduty.com/webhooks/PVN3RMR\",\"html_url\":null},\"incident\":{\"incident_number\":154,\"title\":\"P2 Incident\",\"description\":\"P2 Incident\",\"created_at\":\"2020-08-11T16:09:36Z\",\"status\":\"triggered\",\"incident_key\":\"bcf02a37e41d40f1a5be4b896194ea6c\",\"service\":{\"id\":\"PZDFEG1\",\"name\":\"TestService\",\"description\":null,\"created_at\":\"2020-08-06T19:54:36Z\",\"updated_at\":\"2020-08-06T19:54:36Z\",\"status\":\"critical\",\"teams\":[],\"alert_creation\":\"create_alerts_and_incidents\",\"addons\":[],\"scheduled_actions\":[],\"support_hours\":null,\"last_incident_timestamp\":\"2020-08-11T16:09:36Z\",\"escalation_policy\":{\"id\":\"P3IWEUA\",\"type\":\"escalation_policy_reference\",\"summary\":\"Dummy EP\",\"self\":\"https://api.pagerduty.com/escalation_policies/P3IWEUA\",\"html_url\":\"https://example_pd_domain.pagerduty.com/escalation_policies/P3IWEUA\"},\"incident_urgency_rule\":{\"type\":\"constant\",\"urgency\":\"high\"},\"acknowledgement_timeout\":null,\"auto_resolve_timeout\":null,\"alert_grouping\":null,\"alert_grouping_timeout\":null,\"integrations\":[],\"metadata\":{},\"response_play\":null,\"type\":\"service\",\"summary\":\"TestService\",\"self\":\"https://api.pagerduty.com/services/PZDFEG1\",\"html_url\":\"https://example_pd_domain.pagerduty.com/service-directory/PZDFEG1\"},\"assignments\":[{\"at\":\"2020-08-11T16:09:36Z\",\"assignee\":{\"id\":\"PXNQ3VL\",\"type\":\"user_reference\",\"summary\":\"Giran Moodley\",\"self\":\"https://api.pagerduty.com/users/PXNQ3VL\",\"html_url\":\"https://example_pd_domain.pagerduty.com/users/PXNQ3VL\"}}],\"assigned_via\":\"escalation_policy\",\"last_status_change_at\":\"2020-08-11T16:09:36Z\",\"first_trigger_log_entry\":{\"id\":\"R6O4ZYP1L0TW4JD129TE8KXT6C\",\"type\":\"trigger_log_entry_reference\",\"summary\":\"Triggered through the website\",\"self\":\"https://api.pagerduty.com/log_entries/R6O4ZYP1L0TW4JD129TE8KXT6C\",\"html_url\":\"https://example_pd_domain.pagerduty.com/incidents/PKSEBO6/log_entries/R6O4ZYP1L0TW4JD129TE8KXT6C\"},\"alert_counts\":{\"all\":0,\"triggered\":0,\"resolved\":0},\"is_mergeable\":true,\"escalation_policy\":{\"id\":\"P3IWEUA\",\"type\":\"escalation_policy_reference\",\"summary\":\"Dummy EP\",\"self\":\"https://api.pagerduty.com/escalation_policies/P3IWEUA\",\"html_url\":\"https://example_pd_domain.pagerduty.com/escalation_policies/P3IWEUA\"},\"teams\":[],\"impacted_services\":[{\"id\":\"PZDFEG1\",\"type\":\"service_reference\",\"summary\":\"TestService\",\"self\":\"https://api.pagerduty.com/services/PZDFEG1\",\"html_url\":\"https://example_pd_domain.pagerduty.com/service-directory/PZDFEG1\"}],\"pending_actions\":[],\"acknowledgements\":[],\"basic_alert_grouping\":null,\"alert_grouping\":null,\"last_status_change_by\":{\"id\":\"PZDFEG1\",\"type\":\"service_reference\",\"summary\":\"TestService\",\"self\":\"https://api.pagerduty.com/services/PZDFEG1\",\"html_url\":\"https://example_pd_domain.pagerduty.com/service-directory/PZDFEG1\"},\"metadata\":{},\"external_references\":[],\"priority\":{\"id\":\"PRLXQPW\",\"type\":\"priority\",\"summary\":\"P2\",\"self\":\"https://api.pagerduty.com/priorities/PRLXQPW\",\"html_url\":null,\"account_id\":\"PB6VYZH\",\"color\":\"eb6016\",\"created_at\":\"2020-06-22T21:47:06Z\",\"description\":\"\",\"name\":\"P2\",\"order\":2097152,\"schema_version\":0,\"updated_at\":\"2020-06-22T21:47:06Z\"},\"incidents_responders\":[],\"responder_requests\":[],\"subscriber_requests\":[],\"urgency\":\"high\",\"id\":\"PKSEBO6\",\"type\":\"incident\",\"summary\":\"[#154] P2 Incident\",\"self\":\"https://api.pagerduty.com/incidents/PKSEBO6\",\"html_url\":\"https://example_pd_domain.pagerduty.com/incidents/PKSEBO6\",\"alerts\":[]},\"id\":\"0d5e7528-dbed-11ea-b3e3-0242c0a82a05\",\"created_on\":\"2020-08-11T16:09:36Z\",\"account_features\":{\"response_automation\":true},\"account_id\":\"PB6VYZH\"}]}",
        "isBase64Encoded": False
    }
    lambda_handler(args, None)

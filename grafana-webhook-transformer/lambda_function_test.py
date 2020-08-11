#!/usr/bin/env python3
from lambda_function import lambda_handler

# Run Lambda function using test args through argv.
if __name__ == "__main__":
    args = {
        "version": "2.0",
        "routeKey": "ANY /pdt-giran-grafana-webhook-transformer",
        "rawPath": "/default/pdt-giran-grafana-webhook-transformer",
        "rawQueryString": "routing_key=PD_ROUTING_KEY&severity=info",
        "headers": {
            "accept-encoding": "gzip",
            "content-length": "434",
            "content-type": "application/json",
            "host": "ijghsjizz6.execute-api.us-east-1.amazonaws.com",
            "user-agent": "Grafana",
            "x-amzn-trace-id": "Root=1-5f048915-833b4e0878c8895cbe2e73a0",
            "x-forwarded-for": "82.18.5.181",
            "x-forwarded-port": "443",
            "x-forwarded-proto": "https"
        },
        "queryStringParameters": {
            "routing_key": "PD_ROUTING_KEY",
            "severity": "info"
        },
        "requestContext": {
            "accountId": "864672256020",
            "apiId": "ijghsjizz6",
            "domainName": "ijghsjizz6.execute-api.us-east-1.amazonaws.com",
            "domainPrefix": "ijghsjizz6",
            "http": {
                "method": "POST",
                "path": "/default/pdt-giran-grafana-webhook-transformer",
                "protocol": "HTTP/1.1",
                "sourceIp": "82.18.5.181",
                "userAgent": "Grafana"
            },
            "requestId": "PTpbZi01oAMESRg=",
            "routeKey": "ANY /pdt-giran-grafana-webhook-transformer",
            "stage": "default",
            "time": "07/Jul/2020:14:39:17 +0000",
            "timeEpoch": 1594132757685
        },
        "body": "{\"dashboardId\":1,\"evalMatches\":[{\"value\":100,\"metric\":\"High value\",\"tags\":null},{\"value\":200,\"metric\":\"Higher Value\",\"tags\":null}],\"imageUrl\":\"https://grafana.com/assets/img/blog/mixed_styles.png\",\"message\":\"Someone is testing the alert notification within grafana.\",\"orgId\":0,\"panelId\":1,\"ruleId\":0,\"ruleName\":\"Test notification\",\"ruleUrl\":\"http://localhost:3000/\",\"state\":\"alerting\",\"tags\":{},\"title\":\"[Alerting] Test notification\"}",
        "isBase64Encoded": False
    }
    lambda_handler(args, None)

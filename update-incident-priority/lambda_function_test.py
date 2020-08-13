#!/usr/bin/env python3
from lambda_function import lambda_handler

# Run Lambda function using test args through argv.
if __name__ == "__main__":
    args = {
        "token": "<API_TOKEN>",
        "auth_email": "user@example.com",
        "alert_count": 1
    }
    lambda_handler(args, None)

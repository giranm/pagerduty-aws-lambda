#!/usr/bin/env python3
from lambda_function import lambda_handler

# Run Lambda function using test args through argv.
if __name__ == "__main__":
  args = {
      "token": "<PAGERDUTY_TOKEN>",
      "auth_email": "<PAGERDUTY_LOGIN_EMAIL>",
      "alert_count": 2
  }
  lambda_handler(args, None)

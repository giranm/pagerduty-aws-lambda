#!/usr/bin/env python3
import logging

# Create console logger with timestamp.
logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Set log level and avoid propogation to root AWS logger (e.g. avoid duplication in CloudWatch logs)
logger.setLevel(logging.DEBUG)
logger.propagate = False

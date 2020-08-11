#!/usr/bin/env python3
import logging

# Create console logger with timestamp.
logger = logging.getLogger()
stream_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)

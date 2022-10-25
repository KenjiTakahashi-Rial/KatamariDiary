"""Importing this module will set up the project defaults for logging."""

import logging as logging

DEFAULT_FORMAT = f"[%(levelname)s] %(asctime)s | %(message)s"
DEFAULT_LEVEL = logging.INFO


logging.basicConfig(
    format=DEFAULT_FORMAT,
    level=DEFAULT_LEVEL,
)

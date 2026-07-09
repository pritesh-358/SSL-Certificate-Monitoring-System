"""
====================================================================
SSL Certificate Monitoring System
====================================================================

Logger Module

Author  : Pritesh Thamke
Version : 3.0
"""

# ==================================================================
# IMPORT MODULES
# ==================================================================

import logging
import os

from datetime import datetime
from logging.handlers import RotatingFileHandler

from config_reader import load_config


# ==================================================================
# SETUP LOGGER
# ==================================================================

def setup_logger():

    config = load_config()

    os.makedirs("logs", exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")

    log_file = os.path.join(
        "logs",
        f"ssl_monitor_{today}.log"
    )

    logger = logging.getLogger()

    logger.handlers.clear()

    # ==============================================================
    # LOG LEVEL FROM CONFIG
    # ==============================================================

    log_level = config["logging"]["level"].upper()

    logger.setLevel(getattr(logging, log_level))

    # ==============================================================
    # FORMATTER
    # ==============================================================

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    # ==============================================================
    # FILE HANDLER
    # ==============================================================

    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    # ==============================================================
    # CONSOLE HANDLER
    # ==============================================================

    if config["logging"]["console"]:

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger
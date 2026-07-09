"""
====================================================================
Configuration Reader
====================================================================

Author  : Pritesh Thamke
Version : 3.0

Description
-----------
Reads configuration from config/config.yaml

====================================================================
"""

# ==================================================================
# IMPORT MODULES
# ==================================================================

import os
import yaml


# ==================================================================
# CONFIG FILE PATH
# ==================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_FILE = os.path.join(
    BASE_DIR,
    "config",
    "config.yaml"
)


# ==================================================================
# LOAD CONFIGURATION
# ==================================================================

def load_config():
    """
    Load configuration from config.yaml

    Returns
    -------
    dict
        Configuration Dictionary
    """

    try:

        with open(CONFIG_FILE, "r", encoding="utf-8") as file:

            config = yaml.safe_load(file)

        return config

    except FileNotFoundError:

        raise FileNotFoundError(
            f"Configuration file not found:\n{CONFIG_FILE}"
        )

    except yaml.YAMLError as error:

        raise Exception(
            f"Invalid YAML Configuration.\n\n{error}"
        )

    except Exception as error:

        raise Exception(
            f"Unable to load configuration.\n\n{error}"
        )


# ==================================================================
# GET PROJECT INFORMATION
# ==================================================================

def get_project_info():

    config = load_config()

    return config["project"]


# ==================================================================
# GET SCAN CONFIGURATION
# ==================================================================

def get_scan_config():

    config = load_config()

    return config["scan"]


# ==================================================================
# GET REPORT CONFIGURATION
# ==================================================================

def get_report_config():

    config = load_config()

    return config["reports"]


# ==================================================================
# GET EMAIL CONFIGURATION
# ==================================================================

def get_email_config():

    config = load_config()

    return config["email"]


# ==================================================================
# GET LOGGING CONFIGURATION
# ==================================================================

def get_logging_config():

    config = load_config()

    return config["logging"]


# ==================================================================
# GET APPLICATION CONFIGURATION
# ==================================================================

def get_application_config():

    config = load_config()

    return config["application"]


# ==================================================================
# GET DASHBOARD CONFIGURATION
# ==================================================================

def get_dashboard_config():

    config = load_config()

    return config["dashboard"]


# ==================================================================
# GET NOTIFICATION CONFIGURATION
# ==================================================================

def get_notification_config():

    config = load_config()

    return config["notification"]


# ==================================================================
# GET PERFORMANCE CONFIGURATION
# ==================================================================

def get_performance_config():

    config = load_config()

    return config["performance"]


# ==================================================================
# TEST CONFIGURATION
# ==================================================================

if __name__ == "__main__":

    configuration = load_config()

    print("=" * 70)

    print("Configuration Loaded Successfully")

    print("=" * 70)

    print(configuration)

    print("=" * 70)
from os import environ as env

APP_NAME = env.get("EPST_APP_NAME", "inspirationalshitpost")

# Valid values are 'debug', 'info', 'warn', 'error', or 'critical'
LOG_LEVEL = env.get("EPST_LOG_LEVEL", "info").lower()

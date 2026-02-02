import os

# Base directory of the project
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Directories
LOGICS_DIR = os.path.join(BASE_DIR, 'logics')
HISTORY_DIR = os.path.join(BASE_DIR, 'history')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

# File paths
HISTORY_FILE = os.path.join(HISTORY_DIR, 'operations.json')
AUDIT_LOG_FILE = os.path.join(LOGS_DIR, 'audit.log')

# Ensure directories exist
os.makedirs(HISTORY_DIR, exist_ok=True)
os.makedirs(LOGS_DIR, exist_ok=True)

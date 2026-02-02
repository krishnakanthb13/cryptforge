import logging
import os
import datetime
from config import AUDIT_LOG_FILE

def setup_logging():
    """Configures the logging system."""
    logging.basicConfig(
        filename=AUDIT_LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

def log_operation(operation: str, file_path: str, logic: str, status: str, message: str = ""):
    """Logs an encryption/decryption operation."""
    log_msg = f"Operation: {operation}, File: {file_path}, Logic: {logic}, Status: {status}"
    if message:
        log_msg += f", Message: {message}"
    logging.info(log_msg)

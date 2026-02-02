#!/bin/bash

# -----------------------------------------------------------------------------
# CryptForge Launcher for Linux/macOS
# Checks environment and launches the tool.
# -----------------------------------------------------------------------------

APP_NAME="CryptForge"
ENTRY_POINT="main.py"

# Function to print messages
log_info() { echo -e "\033[1;34m[INFO]\033[0m $1"; }
log_error() { echo -e "\033[1;31m[ERROR]\033[0m $1"; }

# 1. Graceful Shutdown (Trap Signals)
cleanup() {
    # Kill child processes if any
    pkill -P $$
    exit 0
}
trap cleanup SIGINT SIGTERM

# 2. Check for Python
if ! command -v python3 &> /dev/null; then
    log_error "Python 3 is not installed or not in PATH."
    exit 1
fi

# 3. Check for Requirements
# Check if cryptography is installed
if ! python3 -c "import cryptography" &> /dev/null; then
    log_info "Dependencies missing. Installing from requirements.txt..."
    pip3 install -r requirements.txt
    if [ $? -ne 0 ]; then
        log_error "Failed to install dependencies. You may need 'sudo' or use a venv."
        exit 1
    fi
    log_info "Dependencies installed."
fi

# 4. Launch Application
log_info "Starting $APP_NAME..."
python3 "$ENTRY_POINT" "$@"

# Exit with the status of the last command
exit $?

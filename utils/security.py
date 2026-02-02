import getpass
import sys

def get_secure_password(prompt: str = "Enter password: ", confirm: bool = False) -> str:
    """
    Securely gets a password from the user without echoing.
    
    Args:
        prompt (str): The prompt to display.
        confirm (bool): If True, asks for confirmation (useful for encryption).
        
    Returns:
        str: The entered password.
    """
    if not sys.stdin.isatty():
        # Handle non-interactive mode (e.g. piped input)
        # Warning: This might echo if not handled by shell, but standard for CLI tools
        # allowing piping.
        return sys.stdin.readline().strip()
        
    while True:
        password = getpass.getpass(prompt)
        if not password:
            print("Password cannot be empty. Please try again.")
            continue
            
        if confirm:
            confirm_pass = getpass.getpass("Confirm password: ")
            if password != confirm_pass:
                print("Passwords do not match. Please try again.")
                continue
                
        return password

import sys
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def add_context_menu():
    """
    Adds 'Encrypt/Decrypt with CryptForge' to the Windows context menu.
    Requires Admin privileges.
    """
    if sys.platform != 'win32':
        print("Error: Context menu integration is only supported on Windows for now.")
        return

    if not is_admin():
        print("Error: Access denied. Please run this command as Administrator.")
        return

    try:
        import winreg
    except ImportError:
        print("Error: winreg module not found.")
        return

    # Path to launcher.bat
    # We assume launcher.bat is in the same directory as main.py (root)
    # This script is in utils/, so we go up one level
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    launcher_path = os.path.join(base_dir, "launcher.bat")
    icon_path = os.path.join(base_dir, "assets", "icon.ico") # Placeholder
    
    if not os.path.exists(launcher_path):
        print(f"Error: Launcher not found at {launcher_path}")
        return

    key_path = r"*\shell\CryptForge"
    
    try:
        # Create the main key
        key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path)
        winreg.SetValue(key, "", winreg.REG_SZ, "CryptForge Operations")
        winreg.SetValueEx(key, "Icon", 0, winreg.REG_SZ, "shell32.dll,48") # Generic lock icon
        winreg.CloseKey(key)
        
        # Create 'Encrypt' command
        enc_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path + r"\shell\Encrypt")
        winreg.SetValue(enc_key, "", winreg.REG_SZ, "Encrypt File")
        cmd_key = winreg.CreateKey(enc_key, "command")
        winreg.SetValue(cmd_key, "", winreg.REG_SZ, f'"{launcher_path}" encrypt "%1"')
        winreg.CloseKey(cmd_key)
        winreg.CloseKey(enc_key)

        # Create 'Decrypt' command
        dec_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, key_path + r"\shell\Decrypt")
        winreg.SetValue(dec_key, "", winreg.REG_SZ, "Decrypt File")
        cmd_key = winreg.CreateKey(dec_key, "command")
        winreg.SetValue(cmd_key, "", winreg.REG_SZ, f'"{launcher_path}" decrypt "%1"')
        winreg.CloseKey(cmd_key)
        winreg.CloseKey(dec_key)
        
        print("Successfully added CryptForge to context menu!")
        
    except Exception as e:
        print(f"Error modifying registry: {e}")

def remove_context_menu():
    """Removes CryptForge keys from registry."""
    if not is_admin():
        print("Error: Access denied. Please run this command as Administrator.")
        return
        
    try:
        import winreg
        key_path = r"*\shell\CryptForge"
        # Deleting keys recursively is tricky in winreg.
        # Simple implementation: Delete subkeys then main key
        # This is a bit simplified, production usage might need robust recursion
        
        base_key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, r"*\shell", 0, winreg.KEY_ALL_ACCESS)
        try:
            winreg.DeleteKey(base_key, "CryptForge") # Only works if empty? reg delete is easier via subprocess
        except OSError:
             # Use reg delete command for recursive deletion
            os.system(r'reg delete "HKCR\*\shell\CryptForge" /f')
            
        print("Successfully removed CryptForge from context menu.")
        
    except Exception as e:
        print(f"Error removing from registry: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "remove":
        remove_context_menu()
    else:
        add_context_menu()

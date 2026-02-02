import argparse
import sys
import os
from utils.plugin_loader import load_logics
from utils.security import get_secure_password
from utils.file_ops import read_file, write_file
from utils.logging import setup_logging, log_operation
from utils.history import save_history_entry, get_recent_history

def run():
    """
    Main CLI execution function.
    """
    setup_logging()
    available_logics = load_logics()
    
    parser = argparse.ArgumentParser(
        description="CryptForge: Modular Encryption & Decryption CLI Tool"
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Encrypt Command
    encrypt_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    encrypt_parser.add_argument("file", help="Path to the file to encrypt")
    encrypt_parser.add_argument("--logic", help="Encryption logic to use (default: aes)", default="aes")
    
    # Decrypt Command
    decrypt_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    decrypt_parser.add_argument("file", help="Path to the file to decrypt")
    decrypt_parser.add_argument("--logic", help="Decryption logic to use (default: aes)", default="aes")
    
    # History Command
    history_parser = subparsers.add_parser("history", help="View operation history")
    history_parser.add_argument("--last", type=int, help="Show last N operations", default=10)
    
    # List Logics Command
    subparsers.add_parser("logics", help="List available encryption logics")

    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        sys.exit(0)

    # Dispatch commands
    if args.command == "encrypt":
        try:
            logic_cls = available_logics.get(args.logic)
            if not logic_cls:
                print(f"Error: Logic '{args.logic}' not found.")
                sys.exit(1)
            
            logic = logic_cls()
            print(f"Encrypting '{args.file}' using {logic.name}...")
            
            data = read_file(args.file)
            password = get_secure_password("Enter encryption password: ", confirm=True)
            
            encrypted_data = logic.encrypt(data, password)
            
            output_path = f"{args.file}.enc"
            write_file(output_path, encrypted_data, overwrite=False)
            print(f"Success! Encrypted file saved to: {output_path}")
            
            log_operation("encrypt", args.file, logic.name, "success")
            save_history_entry("encrypt", args.file, logic.name, "success")
            
        except (ValueError, FileNotFoundError, FileExistsError, IOError) as e:
            print(f"Error: {e}")
            log_operation("encrypt", args.file, args.logic, "failure", str(e))
            save_history_entry("encrypt", args.file, args.logic, "failure")
            sys.exit(1)
            
    elif args.command == "decrypt":
        try:
            logic_cls = available_logics.get(args.logic)
            if not logic_cls:
                print(f"Error: Logic '{args.logic}' not found.")
                sys.exit(1)
            
            logic = logic_cls()
            print(f"Decrypting '{args.file}' using {logic.name}...")
            
            data = read_file(args.file)
            password = get_secure_password("Enter decryption password: ", confirm=False)
            
            decrypted_data = logic.decrypt(data, password)
            
            # Remove .enc extension if present, otherwise append .dec
            if args.file.endswith(".enc"):
                output_path = args.file[:-4]
            else:
                output_path = f"{args.file}.dec"
                
            write_file(output_path, decrypted_data, overwrite=False)
            print(f"Success! Decrypted file saved to: {output_path}")
            
            log_operation("decrypt", args.file, logic.name, "success")
            save_history_entry("decrypt", args.file, logic.name, "success")
            
        except (ValueError, FileNotFoundError, FileExistsError, IOError) as e:
            print(f"Error: {e}")
            log_operation("decrypt", args.file, args.logic, "failure", str(e))
            save_history_entry("decrypt", args.file, args.logic, "failure")
            sys.exit(1)
    elif args.command == "history":
        history = get_recent_history(args.last)
        print(f"Last {len(history)} Operations:")
        print("-" * 60)
        print(f"{'Timestamp':<25} | {'Op':<8} | {'Logic':<6} | {'Status':<8} | {'File'}")
        print("-" * 60)
        for entry in reversed(history): # Show newest first
            timestamp = entry.get('timestamp', '')[:19] # Truncate microseconds
            print(f"{timestamp:<25} | {entry.get('operation'):<8} | {entry.get('logic'):<6} | {entry.get('status'):<8} | {os.path.basename(entry.get('file_path', ''))}")
    elif args.command == "logics":
        print(f"Available Logics ({len(available_logics)}):")
        for name, logic_cls in available_logics.items():
            # Instantiate to get description
            logic = logic_cls()
            print(f"  - {name}: {logic.description}")

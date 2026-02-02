import os
import sys
from utils.plugin_loader import load_logics
from utils.security import get_secure_password
from utils.file_ops import read_file, write_file
from utils.logging import log_operation
from utils.history import save_history_entry

def display_menu(title, options, columns=3):
    """Displays a numbered menu in multiple columns."""
    print(f"\n{'='*42}")
    print(f"       {title}")
    print(f"{'='*42}")
    
    # Calculate rows
    n = len(options)
    rows = (n + columns - 1) // columns
    
    for r in range(rows):
        line = ""
        for c in range(columns):
            idx = r + c * rows
            if idx < n:
                opt = options[idx]
                # If option already starts with a number (e.g. "0. Exit"), don't add another index
                if opt and opt[0].isdigit() and ". " in opt:
                    entry = f" {opt}"
                else:
                    entry = f"{idx + 1:2}. {opt}"
                line += f"{entry:<18}" # Column width
        print(line)
    print(f"{'='*42}")

def run_interactive_menu():
    """Main interactive loop for the TUI."""
    available_logics = load_logics()
    logic_names = sorted(available_logics.keys())
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_menu("CryptForge - Main Menu", 
                     ["Encrypt a File", "Decrypt a File", "View History", "List Logics", "Help", "0. Exit"], 
                     columns=1)
        
        choice = input("\nSelect an option (0-5): ").strip()
        
        if choice == '0':
            print("Goodbye!")
            break
            
        if choice in ('1', '2'):
            op = "encrypt" if choice == '1' else "decrypt"
            file_path = input(f"\nEnter file path to {op}: ").strip()
            if not os.path.exists(file_path):
                print(f"Error: File '{file_path}' not found.")
                input("\nPress Enter to return to menu...")
                continue
            
            # Select Logic
            display_menu(f"Select {op.capitalize()} Logic", logic_names, columns=3)
            l_choice = input(f"\nSelect logic number (1-{len(logic_names)}) or 'd' for details [Default: aes]: ").strip()
            
            if l_choice.lower() == 'd':
                display_logic_details(available_logics, logic_names)
                input("\nPress Enter to return to selection...")
                # Re-do the encryption/decryption flow logic selection
                continue

            if not l_choice:
                selected_name = "aes"
            else:
                try:
                    idx = int(l_choice) - 1
                    if 0 <= idx < len(logic_names):
                        selected_name = logic_names[idx]
                    else:
                        print("Invalid selection. Using default: aes")
                        selected_name = "aes"
                except ValueError:
                    print("Invalid input. Using default: aes")
                    selected_name = "aes"
            
            # Execute
            try:
                logic_cls = available_logics.get(selected_name)
                logic = logic_cls()
                print(f"\nExecuting {op} using {selected_name}...")
                
                data = read_file(file_path)
                password = get_secure_password(f"Enter {op} password: ", confirm=(op == "encrypt"))
                
                result_data = logic.encrypt(data, password) if op == "encrypt" else logic.decrypt(data, password)
                
                if op == "encrypt":
                    output_path = f"{file_path}.enc"
                else:
                    output_path = file_path[:-4] if file_path.endswith(".enc") else f"{file_path}.dec"
                
                write_file(output_path, result_data, overwrite=False)
                print(f"\n[SUCCESS] Result saved to: {output_path}")
                
                log_operation(op, file_path, selected_name, "success")
                save_history_entry(op, file_path, selected_name, "success")
            except Exception as e:
                print(f"\n[ERROR] {e}")
                log_operation(op, file_path, selected_name, "failure", str(e))
                save_history_entry(op, file_path, selected_name, "failure")
            
            input("\nPress Enter to return to menu...")
            
        elif choice == '3':
            from utils.history import get_recent_history
            history = get_recent_history(10)
            print(f"\nLast {len(history)} Operations:")
            print("-" * 65)
            print(f"{'Timestamp':<20} | {'Op':<8} | {'Logic':<10} | {'Status'}")
            print("-" * 65)
            for entry in reversed(history):
                print(f"{entry.get('timestamp')[:19]:<20} | {entry.get('operation'):<8} | {entry.get('logic'):<10} | {entry.get('status')}")
            input("\nPress Enter to return to menu...")
            
        elif choice == '4':
            display_logic_details(available_logics, logic_names)
            input("\nPress Enter to return to menu...")

        elif choice == '5':
            display_help()
            input("\nPress Enter to return to menu...")
        else:
            print("Invalid option.")
            input("\nPress Enter to return to menu...")

def display_logic_details(available_logics, sorted_names):
    """Displays names and descriptions of all logics."""
    print(f"\n{'='*65}")
    print(f"{'Logic Name':<15} | {'Description'}")
    print(f"{'='*65}")
    for name in sorted_names:
        logic = available_logics[name]()
        print(f"{name:<15} | {logic.description}")
    print(f"{'='*65}")

def display_help():
    """Displays TUI help information."""
    print(f"\n{'='*42}")
    print("           CryptForge Help")
    print(f"{'='*42}")
    print("1. Encrypt: Securely scramble a file.")
    print("   Output will be [filename].enc")
    print("\n2. Decrypt: Restore an encrypted file.")
    print("   Input should be a .enc file.")
    print("\n3. History: View your last 10 operations")
    print("   with timestamps and status.")
    print("\n4. Logics: CryptForge supports over")
    print("   38 different encryption methods.")
    print("\n5. CLI Mode: You can also skip this TUI")
    print("   by passing arguments directly:")
    print("   main.py encrypt file.txt --logic aes")
    print(f"{'='*42}")

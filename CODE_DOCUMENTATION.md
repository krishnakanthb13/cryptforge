# CryptForge Code Documentation

## Project Structure

```
cryptforge/
├── main.py                 # Entry point
├── cli.py                  # CLI argument parsing & command dispatch
├── launcher.bat/sh         # Cross-platform launchers
├── logics/                 # Encryption Logic Plugins
│   ├── base.py             # Abstract Base Class (EncryptionLogic)
│   ├── aes.py              # AES Implementation
│   ├── ciphers.py          # Classic Ciphers (Caesar, Vigenère...)
│   ├── encodings.py        # Encodings (Base64, Hex...)
│   └── ...
├── utils/                  # Utilities
│   ├── plugin_loader.py    # Dynamic plugin discovery
│   ├── security.py         # Password handling
│   ├── file_ops.py         # File I/O
│   └── history.py          # JSON History tracking
└── ...
```

## Core Modules

### 1. Plugin System (`utils/plugin_loader.py`)
This module scans the `logics/` directory for any class inheriting from `EncryptionLogic`.
It allows the system to auto-discover new algorithms without manual registration.

**Flow**:
`CLI` -> `load_logics()` -> `Import modules in logics/*.py` -> `Register valid classes` -> `Return Dict[name, class]`

### 2. Encryption Logic (`logics/base.py`)
The `EncryptionLogic` abstract base class enforces a standard interface:
*   `name`: Unique identifier (e.g., 'aes').
*   `description`: Help text.
*   `encrypt(data, password)`: Returns bytes. Handles data transformation.
*   `decrypt(data, password)`: Returns bytes. Reverses the transformation.
    *   *Note*: Some logics (like Enigma) are symmetric/reciprocal, where encryption and decryption use the same mathematical function.

### 3. CLI Dispatch (`cli.py`)
Uses `argparse` to handle user input and orchestrates the encryption/decryption process.
*   **Encrypt**: Loads logic -> Reads file -> Prompts password -> Encrypts -> Writes `.enc` file.
*   **Decrypt**: Loads logic -> Reads file -> Prompts password -> Decrypts -> Writes decoded file.
*   **Error Handling**: Specifically catches `ValueError`, `FileNotFoundError`, `FileExistsError`, and `IOError` to provide user-friendly messages while allowing system signals (like Ctrl+C) to pass through.

## Data Flow

1.  **Input**: File Path + Logic Name + Password.
2.  **Processing**:
    *   File read as binary (`rb`).
    *   Logic instantiated.
    *   Transformation applied (`logic.encrypt` / `logic.decrypt`).
3.  **Output**:
    *   Result written to disk.
    *   Operation logged to `logs/`.
    *   History updated in `history/`.

## Dependencies
*   **cryptography**: Used for `AESLogic` (AES-256-GCM) and key derivation (PBKDF2).
*   **Standard Lib**: `argparse`, `json`, `os`, `sys`, `importlib`.

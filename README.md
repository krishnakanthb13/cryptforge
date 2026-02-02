# CryptForge
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A modular, cross-platform CLI tool for encryption, decryption, and encoding. Built with Python.

## Features
*   **Production Grade**: Secure AES-256-GCM encryption with PBKDF2 key derivation.
*   **Classic Ciphers**: Caesar, Vigenère, Enigma Machine, Rail Fence, Bacon, and more.
*   **Encodings**: Base64, Hex, Binary, Morse Code, Baudot, Punycode, Bootstring.
*   **Polybius Variants**: ADFGX, Nihilist, Bifid, Trifid, Tap Code.
*   **Robust CLI**: Clean error handling, operation history, and audit logging.
*   **Extensible**: Easily add new logic via the modular plugin system.

## Quick Start
1.  **Clone the repo**:
    ```bash
    git clone https://github.com/krishnakanthb13/cryptforge.git
    cd cryptforge
    ```
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run**:
    ```bash
    # See help
    python main.py --help
    
    # List available ciphers
    python main.py logics
    ```

## Usage Examples

**Encrypt with AES (Default)**
```bash
python main.py encrypt secret.txt
# Prompts for password...
```

**Use a specific cipher (e.g., Morse Code)**
```bash
python main.py encrypt message.txt --logic morse
```

**Decrypt**
```bash
python main.py decrypt message.txt.enc --logic morse
```

## Documentation
*   [**Design Philosophy**](DESIGN_PHILOSOPHY.md): Why we built this.
*   [**Code Documentation**](CODE_DOCUMENTATION.md): How it works under the hood.
*   [**Contributing**](CONTRIBUTING.md): How to join the project.

## License
Copyright (C) 2026 Krishna Kanth B.
This project is licensed under the [GNU General Public License v3.0](LICENSE).

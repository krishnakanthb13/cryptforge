# CryptForge
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A modular, cross-platform CLI tool for encryption, decryption, and encoding. Built with Python.

```
==========================================
       CryptForge - Main Menu
==========================================
 1. Encrypt a File
 2. Decrypt a File
 3. View History  
 4. List Logics   
 5. Help          
 0. Exit          
==========================================

==========================================
       Select Encrypt Logic
==========================================
 1. a1z26         14. caesar        27. railfence     
 2. adfgx         15. case          28. rc4           
 3. aes           16. enigma        29. replace       
 4. affine        17. hash          30. reverse       
 5. ascii85       18. hex           31. rot13         
 6. bacon         19. hmac          32. substitution  
 7. base32        20. integer       33. tapcode       
 8. base64        21. morse         34. trifid        
 9. baudot        22. nato          35. unicode       
10. bifid         23. nihilist      36. url           
11. bitwise       24. numeral       37. vigenere      
12. blowfish      25. polybius      38. xor           
13. bootstring    26. punycode      
==========================================
```

## Features
*   **Production Grade**: Secure AES-256-GCM encryption with PBKDF2 key derivation.
*   **Classic Ciphers**: Caesar, Vigenère, Enigma Machine, Rail Fence, Bacon, and more.
*   **Encodings**: Base64, Hex, Binary, Morse Code, Baudot, Punycode, Bootstring.
*   **Polybius Variants**: ADFGX, Nihilist, Bifid, Trifid, Tap Code.
*   **Robust CLI**: Clean error handling, operation history, and audit logging.
*   **Interactive TUI**: Easy-to-use terminal menu for guided operations and logic selection.
*   **Automated Testing**: Built-in test suite covering all 38+ logics with detailed logging.
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
    # Run Interactive Menu (Recommended for New Users)
    ./launcher.bat  # Windows
    ./launcher.sh   # Linux/macOS
    
    # Or use direct CLI commands
    python main.py --help
    ```

4. **Install as CLI Tool (Optional)**:
   ```bash
   pip install .
   # Now you can use 'cryptforge' from anywhere!
   cryptforge menu
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

## Running Tests
CryptForge comes with a comprehensive automated test suite.

**Via Interactive Menu:**
Launch the launcher and select **"Run Unit Tests" (Option 6)**.

**Via CLI:**
```bash
python unit_tests/run_all.py
```
This will generate a summary log in `unit_tests/test_run.log`.

## Documentation
*   [**Design Philosophy**](DESIGN_PHILOSOPHY.md): Why we built this.
*   [**Code Documentation**](CODE_DOCUMENTATION.md): How it works under the hood.
*   [**Contributing**](CONTRIBUTING.md): How to join the project.

## License
Copyright (C) 2026 Krishna Kanth B.
This project is licensed under the [GNU General Public License v3.0](LICENSE).

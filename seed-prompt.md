Encryption & Decryption.
- Various logics. Each logic different python file in a folder.
- CLI tool, navigate to directory and files.
- history mode.
- Logging file location, logic used, date and time encrypt or decrypt.
- Password saved separate - Bit-warden.
- Right click context menu launcher.

---

Below is a **precision-engineered master prompt** you can directly give to another AI (or reuse yourself) to design and implement this system.
I’m **not** solving the task — this is the optimized prompt that will.

---

## 🔐 OPTIMIZED PROMPT: Modular Encryption & Decryption CLI Tool (Python)

### ROLE

You are a **senior Python security engineer + CLI UX designer** experienced in encryption systems, modular architectures, and cross-platform tooling.

---

### OBJECTIVE

Design and implement a **modular Encryption & Decryption CLI tool in Python** with pluggable encryption logics, strong audit logging, history tracking, and OS-level usability enhancements.

---

### CORE REQUIREMENTS

#### 1. **Modular Encryption Logic System**

* Each encryption/decryption logic must be:

  * Implemented as a **separate Python file**
  * Stored inside a dedicated folder (e.g. `logics/`)
  * Follow a **standard interface / contract**, such as:

    * `encrypt(data, password)`
    * `decrypt(data, password)`
* CLI should **auto-discover available logic files** dynamically
* Allow easy addition/removal of logics without touching core code

---

#### 2. **CLI Tool**

* Executable via terminal (e.g. `encryptor`)
* Features:

  * Navigate directories and files
  * Select file(s) for encryption or decryption
  * Choose encryption logic interactively or via flags
* Example usage:

  ```
  encryptor encrypt ./file.txt --logic aes
  encryptor decrypt ./file.enc --logic xor
  encryptor history
  ```

---

#### 3. **History Mode**

* Maintain a **persistent history** of operations
* History command should show:

  * File path
  * Encryption logic used
  * Operation (encrypt/decrypt)
  * Date & time
  * Status (success/failure)
* History must be readable via:

  ```
  encryptor history
  encryptor history --last 10
  ```

---

#### 4. **Logging System**

* Central logging mechanism that records:

  * File location
  * Logic used
  * Timestamp
  * Operation type (encrypt/decrypt)
* Logs should be:

  * Written to a configurable file location
  * Structured (JSON preferred)
  * Append-only
* Include log rotation strategy

---

#### 5. **Password Handling (Security Constraint)**

* **Passwords must NOT be stored**
* Passwords are:

  * Retrieved at runtime
  * Stored externally using **Bitwarden**
* Tool should:

  * Accept password input securely (no echo)
  * Optionally integrate with Bitwarden CLI (`bw`) if available
  * Clearly document password flow and security assumptions

---

#### 6. **Right-Click Context Menu Launcher**

* Enable launching the tool via **right-click context menu**:

  * On files and folders
* Design for:

  * Windows (registry-based solution)
  * Linux (desktop entry / Nautilus / KDE)
  * macOS (Finder service – optional)
* Context menu action should:

  * Open terminal
  * Invoke CLI with selected file path

---

### ARCHITECTURE REQUIREMENTS

* Clear folder structure (example):

  ```
  encryptor/
  ├── main.py
  ├── cli.py
  ├── logics/
  │   ├── aes.py
  │   ├── xor.py
  ├── history/
  ├── logs/
  ├── utils/
  ```
* Separation of concerns:

  * CLI parsing
  * Logic loading
  * Encryption engine
  * Logging & history
* Code must be:

  * Extensible
  * Well-documented
  * Cross-platform friendly

---

### OUTPUT EXPECTATIONS

Provide:

1. High-level system architecture
2. Folder structure explanation
3. CLI command design
4. Plugin/logic interface specification
5. Logging & history format examples
6. Security considerations
7. OS-specific notes for right-click integration

---

### CONSTRAINTS

* Python only
* No GUI (CLI-first)
* No password persistence
* Assume intermediate to advanced user

---

### QUALITY BAR

* Production-grade design
* Security-conscious defaults
* Clear extension points
* Minimal hardcoding

---

### OPTIONAL ENHANCEMENTS (If Relevant)

* Dry-run mode
* Batch operations
* Config file support
* Logic benchmarking mode

---

**Execute this task step-by-step with clear reasoning and structured output.**

---
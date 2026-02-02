# Contributing to CryptForge

First off, thank you for considering contributing to CryptForge! It's people like you who make it a great tool.

## How Can I Contribute?

### Adding New Encryption Logics
The easiest way to contribute is by adding new algorithms!
1. Check the `logics/` directory to see existing implementations.
2. Create a new file (or add to an existing one) in `logics/`.
3. Inherit from `EncryptionLogic` in `logics/base.py`.
4. Implement the `encrypt` and `decrypt` methods.
5. Add a unit test in `unit_tests/` (following the existing patterns).

### Reporting Bugs
If you find a bug, please open an issue on GitHub. Include:
- Your operating system.
- The command you ran.
- The error message or unexpected behavior.

### Suggesting Enhancements
We are always looking for ways to make CryptForge better. Suggest new features or UI improvements by opening an issue.

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/krishnakanthb13/cryptforge.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the tests to ensure everything is working:
   ```bash
   python unit_tests/run_all.py
   ```

## Style Guide
- Use Python 3.8+.
- Follow PEP 8 for code style.
- Ensure all new logic classes have a clear `description`.
- Document your code where necessary.

Thank you for contributing! 🛡️

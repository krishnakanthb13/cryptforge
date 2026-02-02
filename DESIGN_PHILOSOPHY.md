# CryptForge Design Philosophy

## 1. The Problem
Encryption tools are often either too complex (OpenSSL), platform-specific, or exist as opaque web tools that shouldn't be trusted with sensitive data. There was a need for a **transparent, local-first, and extensible** CLI tool that handles both classic (ciphers) and modern (AES) encryption.

## 2. The Solution
CryptForge provides a unified interface for various encryption methods. It creates a standardized "Logic" plugin system where `aes`, `xor`, `morse`, and `enigma` can coexist and be used interchangeably.

## 3. Design Principles

*   **Modularity First**: Every encryption algorithm is a class inheriting from `EncryptionLogic`. Adding a new cipher should never require changing the core CLI code.
*   **Transparency**: No "magic" obfuscation. The code does exactly what it says.
*   **User Experience**: Simple commands (`encrypt`, `decrypt`). Interactive password handling for security. Clean output.
*   **Education & Utility**: Supports educational ciphers (Caesar, Enigma) alongside production-grade crypto (AES-256-GCM).
*   **Defensive Design**: Specific exception handling ensures the tool is resilient to user error (invalid paths, bad passwords) without crashing or swallowing system signals.

## 4. Target Audience
*   **Developers**: needing quick encodings/decodings (Base64, Hex).
*   **CTF Players**: solving crypto challenges (Vigenère, Morse, Rail Fence).
*   **Privacy Conscious**: encrypting files locally before cloud upload.

## 5. Trade-offs
*   **Python Runtime**: Chosen for readability and extensibility over raw C/Rust speed. fast enough for typical file sizes (MBs to GBs).
*   **CLI Only**: Focused on automation and terminal dominance. No GUI bloat.

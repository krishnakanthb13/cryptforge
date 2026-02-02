#!/usr/bin/env python3
import sys
import cli

def main():
    """
    Entry point for the CryptForge CLI tool.
    """
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(130)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

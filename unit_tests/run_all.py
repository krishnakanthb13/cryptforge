import unittest
import os
import sys
from datetime import datetime

def run_all_tests():
    # Setup test suite
    loader = unittest.TestLoader()
    start_dir = os.path.dirname(os.path.abspath(__file__))
    suite = loader.discover(start_dir, pattern='test_*.py')

    log_file = os.path.join(start_dir, "test_run.log")
    
    # Run tests and capture results
    with open(log_file, "w") as f:
        f.write(f"CryptForge Unit Test Run - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("="*60 + "\n\n")
        
        # We'll use a TextTestRunner but we want to capture output
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        result = runner.run(suite)
        
        f.write("\n" + "="*60 + "\n")
        f.write(f"Tests Run: {result.testsRun}\n")
        f.write(f"Errors: {len(result.errors)}\n")
        f.write(f"Failures: {len(result.failures)}\n")
        f.write(f"Skipped: {len(result.skipped)}\n")
        
        if result.wasSuccessful():
            f.write("\nSTATUS: ALL TESTS PASSED\n")
        else:
            f.write("\nSTATUS: TESTS FAILED\n")

    # Print summary to console
    print(f"\nTests completed. Summary written to {log_file}")
    if result.wasSuccessful():
        print("Final Status: PASS")
        sys.exit(0)
    else:
        print("Final Status: FAIL")
        sys.exit(1)

if __name__ == "__main__":
    # Ensure the parent directory is in the path so logics can be imported
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    run_all_tests()

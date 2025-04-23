#!/usr/bin/env python
"""
Test runner script for EnginML package.

This script demonstrates how to run the tests and verify that the package works correctly.
It can be used as a quick check to ensure everything is working as expected.
"""
import os
import subprocess
import sys


def main():
    """Run the tests and print the results."""
    print("\n===== Testing EnginML package =====\n")
    
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Change to the script directory
    os.chdir(script_dir)
    
    # Check if pytest is installed
    try:
        import pytest
    except ImportError:
        print("pytest is not installed. Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", ".[full]", "pytest", "pytest-cov"])
    
    print("\n1. Running basic tests...")
    basic_result = subprocess.run([sys.executable, "-m", "pytest", "-v"], capture_output=True, text=True)
    
    if basic_result.returncode == 0:
        print("\n✅ Basic tests passed!")
    else:
        print("\n❌ Some tests failed. See details below:")
        print(basic_result.stdout)
        print(basic_result.stderr)
        return 1
    
    print("\n2. Running tests with coverage...")
    coverage_result = subprocess.run(
        [sys.executable, "-m", "pytest", "--cov=EnginML", "--cov-report=term-missing"],
        capture_output=True,
        text=True
    )
    
    # Print coverage report
    print("\nCoverage Report:")
    for line in coverage_result.stdout.splitlines():
        if "TOTAL" in line or "EnginML/" in line:
            print(line)
    
    print("\n===== All tests completed =====\n")
    print("To run the tests manually, use one of the following commands:")
    print("  pytest                        # Run all tests")
    print("  pytest -v                     # Run all tests with verbose output")
    print("  pytest --cov=EnginML         # Run tests with coverage report")
    print("  pytest tests/test_core.py     # Run specific test file")
    print("  pytest tests/test_core.py::test_fit_regression_random_forest  # Run specific test function")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
"""Pytest configuration file for EnginML tests."""
import os
import pytest


@pytest.fixture(scope="session")
def tmp_dir(tmpdir_factory):
    """Create a temporary directory for test outputs."""
    return tmpdir_factory.mktemp("enginml_test_outputs")


@pytest.fixture(autouse=True)
def cleanup_test_files():
    """Clean up any test files after each test."""
    yield
    # Add any specific cleanup code here if needed
    # This runs after each test function completes
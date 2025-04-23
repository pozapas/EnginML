# Testing Strategy for EnginML

This document outlines the testing strategy for the `EnginML` package, explaining how to run the tests and what they cover.

## Overview

The testing strategy for `EnginML` includes multiple levels of testing to ensure the package works correctly:

1. **Unit Tests**: Test individual functions and components in isolation
2. **Integration Tests**: Test how components work together
3. **End-to-End Tests**: Test complete workflows with realistic data
4. **CLI Tests**: Test the command-line interface

## Test Structure

The tests are organized in the following files:

- `tests/test_core.py`: Unit tests for core ML functionality
- `tests/test_cli.py`: Tests for the command-line interface
- `tests/test_integration.py`: Integration tests for workflows
- `tests/test_end_to_end.py`: End-to-end tests with realistic data
- `tests/conftest.py`: Common test fixtures and configurations
- `tests/sample_data.csv`: Sample data for testing

## Running the Tests

### Prerequisites

Before running the tests, make sure you have the development dependencies installed:

```bash
pip install -e ".[full]" pytest pytest-cov black isort
```

### Running All Tests

To run all tests with the default configuration:

```bash
pytest
```

To run tests with coverage reporting:

```bash
pytest --cov=EnginML
```

### Running Specific Tests

To run a specific test file:

```bash
pytest tests/test_core.py
```

To run a specific test function:

```bash
pytest tests/test_core.py::test_fit_regression_random_forest
```

### Using the Test Runner Scripts

For convenience, several test runner scripts are provided:

- `run_tests.py`: Python script that runs all tests and reports coverage
- `run_tests.bat`: Windows batch script for running tests
- `run_tests.ps1`: PowerShell script for running tests

To use the Python script:

```bash
python run_tests.py
```

To use the PowerShell script on Windows:

```powershell
.\run_tests.ps1
```

## What the Tests Cover

### Unit Tests

The unit tests verify that individual functions work correctly:

- Regression model fitting (Random Forest, KNN)
- Classification model fitting (Random Forest, KNN)
- Clustering model fitting (KMeans, Birch, GMM)
- Data loading from CSV and Excel files
- Report generation

### Integration Tests

The integration tests verify that components work together correctly:

- Complete regression workflow (data loading → model fitting → report generation)
- Complete classification workflow
- Complete clustering workflow

### End-to-End Tests

The end-to-end tests verify that the package works correctly with realistic data:

- Regression with synthetic data that has non-linear relationships
- CLI execution with sample data
- Verification of model performance metrics

### CLI Tests

The CLI tests verify that the command-line interface works correctly:

- Regression task
- Classification task
- Clustering task
- Error handling for invalid inputs

## Test Coverage

The test suite aims to achieve high code coverage, testing all major functionality of the package. To see the current coverage, run:

```bash
pytest --cov=EnginML --cov-report=html
```

This will generate an HTML coverage report in the `htmlcov` directory.

## Adding New Tests

When adding new functionality to the package, please add corresponding tests following these guidelines:

1. Add unit tests for new functions
2. Update integration tests if the new functionality affects existing workflows
3. Add end-to-end tests for new workflows
4. Follow the existing test structure and naming conventions

## Continuous Integration

These tests can be integrated into a CI/CD pipeline to ensure that the package works correctly across different environments and versions of Python.
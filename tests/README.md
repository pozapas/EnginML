# Testing EnginML

This directory contains tests for the `EnginML` package. The tests are written using pytest and cover the core functionality and CLI interface of the package.

## Test Structure

- `test_core.py`: Tests for core ML functionality (regression, classification, clustering, data loading, report generation)
- `test_cli.py`: Tests for the command-line interface

## Running Tests

To run the tests, make sure you have the development dependencies installed:

```bash
pip install -e ".[full]" pytest pytest-cov black isort
```

Then, from the root directory of the project, run:

```bash
pytest
```

To run tests with coverage reporting:

```bash
pytest --cov=EnginML
```

To generate an HTML coverage report:

```bash
pytest --cov=EnginML --cov-report=html
```

The HTML report will be generated in the `htmlcov` directory.

## Test Data

The tests use synthetic data generated using scikit-learn's data generation functions. This ensures that the tests are reproducible and do not depend on external data sources.

## Adding New Tests

When adding new functionality to the package, please add corresponding tests. Follow the existing test structure and naming conventions.

## Continuous Integration

These tests can be integrated into a CI/CD pipeline to ensure that the package works correctly across different environments and versions of Python.
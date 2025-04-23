# Installation Guide for EnginML

This guide provides detailed instructions for installing and setting up the EnginML package.

## Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

## Basic Installation

### Option 1: Install from PyPI (Recommended)

Once the package is published to PyPI, you can install it with:

```bash
pip install EnginML
```

### Option 2: Install from Source

1. Clone or download the repository:

```bash
git clone https://github.com/username/EnginML.git
cd EnginML
```

2. Install the package in development mode:

```bash
pip install -e .
```

## Installing with Optional Dependencies

For full functionality including SHAP explanations and HTML reports:

```bash
pip install EnginML[full]
```

Or if installing from source:

```bash
pip install -e ".[full]"
```

## Verifying Installation

To verify that the installation was successful, run:

```bash
python -c "import EnginML; print(EnginML.__version__)"
```

You should see the version number printed (e.g., `0.1.0`).

## Running the CLI

After installation, the `enginml` command should be available in your terminal:

```bash
enginml --help
```

This should display the help message with available options.

## Troubleshooting

### Common Issues

1. **Missing Dependencies**: If you encounter errors about missing packages, try installing with the full dependencies:

```bash
pip install EnginML[full]
```

2. **Command Not Found**: If the `enginml` command is not found, ensure that your Python scripts directory is in your PATH. Alternatively, you can run the CLI module directly:

```bash
python -m EnginML.cli your_data.csv --task regression --target your_target_column
```

3. **ImportError for Optional Dependencies**: If you see errors related to SHAP or Jinja2, install the optional dependencies:

```bash
pip install shap jinja2
```

## Development Setup

If you want to contribute to the development of EnginML:

1. Install development dependencies:

```bash
pip install -e ".[full]" pytest pytest-cov black isort
```

2. Run tests:

```bash
pytest
```

3. Format code:

```bash
black EnginML
isort EnginML
```
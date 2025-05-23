# EnginML

<p align="center">
  <img src="https://raw.githubusercontent.com/pozapas/EnginML/master/logo.png" alt="EnginML Logo" width="350"/>
</p>

An educational Python package designed to help engineers and students learn and apply baseline machine learning workflows (regression, classification, clustering) even with minimal programming experience. This package reproduces the tutorial in [*AI in Civil Engineering* (2025)](https://doi.org/10.1007/s43503-025-00053-x) by M. Z. Naser.

## Overview

This educational package is designed to make machine learning accessible to engineers and students with minimal programming experience. It provides:

- Simple, one-line functions for common ML tasks
- Automatic data loading from CSV and Excel files
- Built-in model training and evaluation
- Visualization of results and model explanations
- HTML report generation
- Command-line interface for easy use

## Installation

```bash
# Basic installation
pip install EnginML

# With all optional dependencies
pip install EnginML[full]
```

## Quick Start

### Command Line Usage

The simplest way to use EnginML is through the command line:

```bash
# For regression
enginml your_data.csv --task regression --target your_target_column

# For classification
enginml your_data.csv --task classification --target your_target_column

# For clustering
enginml your_data.csv --task clustering --n-clusters 3
```

This will automatically:

1. Load your data
2. Train an appropriate model
3. Evaluate the model
4. Generate an HTML report with visualizations

### Python API Usage

```python
import pandas as pd
from EnginML import fit_regression, save_report

# Load your data
df = pd.read_csv('your_data.csv')

# Prepare features and target
X = df.drop(columns=['target_column']).values
y = df['target_column'].values

# Fit a regression model
result = fit_regression(X, y, model='random_forest')

# Print metrics
print(result['metrics'])

# Save HTML report
save_report(result, X, y, feature_names=df.columns[:-1])
```

## Features

### Supported Tasks

- **Regression**: Predict continuous values

  - Models: Random Forest, K-Nearest Neighbors
  - Metrics: R², MAE
- **Classification**: Predict categorical values

  - Models: Random Forest, K-Nearest Neighbors
  - Metrics: Accuracy, F1 Score
- **Clustering**: Group similar data points

  - Models: K-Means, BIRCH, Gaussian Mixture
  - Metrics: Silhouette Score, Davies-Bouldin Index

### Explainability

The package includes SHAP (SHapley Additive exPlanations) integration for model interpretability, helping engineers understand which features are most important for predictions.

### Visualization

Automatic generation of relevant plots for each task type:

- Regression: Actual vs. Predicted, Residuals, Feature Importance
- Classification: Feature Importance, SHAP Summary
- Clustering: Cluster Assignments

## Advanced Usage

### Customizing Models

```python
from EnginML import fit_classification

# Use K-Nearest Neighbors instead of Random Forest
result = fit_classification(X, y, model='knn')
```

### Disabling SHAP Explanations

```python
result = fit_regression(X, y, explain=False)
```

### Custom Report Path

```python
save_report(result, X, y, output_path='custom_path/my_report.html')
```

## Future Features & Enhancements

We're always thinking about how to make EnginML even more helpful for engineers learning ML! Here are some ideas we're exploring:

- [ ] **More Model Options:** Add other popular and easy-to-understand models (e.g., Linear Regression, Logistic Regression, Decision Trees).
- [ ] **Data Preprocessing Guidance:** Include optional, guided steps for common preprocessing tasks like handling missing values or scaling features.
- [ ] **Interactive Visualizations:** Enhance reports with more interactive plots (e.g., using Plotly or Bokeh).
- [ ] **Hyperparameter Tuning Basics:** Introduce a simple way to experiment with basic hyperparameter tuning for selected models.
- [ ] **Time Series Forecasting:** Add a basic module for introductory time series analysis and forecasting tasks.
- [ ] **Anomaly Detection:** Include simple methods for identifying outliers or anomalies in datasets.
- [ ] **Model Comparison:** Allow users to easily train and compare the performance of multiple models on the same dataset.
- [ ] **Code Generation Snippets:** Offer snippets of the underlying scikit-learn code used, helping users transition to more direct library usage.
- [ ] **Expanded Documentation & Tutorials:** Add more examples and detailed explanations for different engineering domains.

## Requirements

- Python 3.9+
- NumPy
- pandas
- scikit-learn
- matplotlib

### Optional Dependencies

- SHAP (for model explanations)
- Jinja2 (for HTML reports)
- XGBoost (for additional models)

## License

MIT

## Citation

This package is created by Amir Rafe (amir.rafe@usu.edu) based on the paper:

```
Naser, M. Z. (2025). A step-by-step tutorial on machine learning for engineers unfamiliar with programming. AI in Civil Engineering. https://doi.org/10.1007/s43503-025-00053-x
```

If you use this package in your research, please cite the original paper.

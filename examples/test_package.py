#!/usr/bin/env python
"""
Example script to test if EnginML package works correctly.

This script demonstrates how to use the package and verify that it works correctly
by running a simple example with synthetic data.
"""
import os
import numpy as np
import pandas as pd
from sklearn.datasets import make_regression

# Import EnginML functions
try:
    from EnginML import fit_regression, fit_classification, fit_clustering, save_report
except ImportError:
    # If package is not installed, try relative import
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from EnginML import fit_regression, fit_classification, fit_clustering, save_report


def test_package():
    """Run a simple test to verify the package works correctly."""
    print("\n===== Testing EnginML package =====\n")
    
    # Create synthetic regression data
    print("Creating synthetic regression data...")
    X, y = make_regression(
        n_samples=100,
        n_features=5,
        n_informative=3,
        random_state=42
    )
    feature_names = [f"feature_{i}" for i in range(X.shape[1])]
    
    # Fit regression model
    print("\nFitting Random Forest regression model...")
    result = fit_regression(X, y, model="random_forest")
    
    # Print metrics
    print("\nModel Performance:")
    for name, value in result["metrics"].items():
        print(f"  {name}: {value:.4f}")
    
    # Save report
    print("\nGenerating HTML report...")
    report_path = save_report(
        result, X, y, 
        task_type="regression",
        feature_names=feature_names,
        output_path="test_report.html"
    )
    print(f"Report saved to: {report_path}")
    
    # Verify the report was created
    if os.path.exists(report_path) and os.path.getsize(report_path) > 0:
        print("\n✅ Test passed! The package is working correctly.")
    else:
        print("\n❌ Test failed! The report was not generated.")
    
    return report_path


if __name__ == "__main__":
    report_path = test_package()
    print(f"\nOpen {report_path} in a web browser to view the report.")
    print("\nTo run the full test suite, use one of the following commands:")
    print("  python run_tests.py")
    print("  pytest")
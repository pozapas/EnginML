"""Simple example demonstrating EnginML usage."""
import numpy as np
import pandas as pd
from sklearn.datasets import load_boston, load_iris, make_blobs

# Import EnginML functions
try:
    from EnginML import fit_regression, fit_classification, fit_clustering, save_report
except ImportError:
    # If package is not installed, try relative import
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from EnginML import fit_regression, fit_classification, fit_clustering, save_report


def regression_example():
    """Demonstrate regression workflow."""
    print("\n=== Regression Example ===")
    
    # Load Boston housing dataset (or create synthetic data if not available)
    try:
        boston = load_boston()
        X, y = boston.data, boston.target
        feature_names = boston.feature_names
    except:
        # Create synthetic data if Boston dataset is not available
        print("Boston dataset not available, using synthetic data")
        np.random.seed(42)
        X = np.random.rand(100, 5)
        y = 5 * X[:, 0] + 3 * X[:, 1] - 2 * X[:, 2] + np.random.randn(100) * 0.5
        feature_names = [f'Feature_{i}' for i in range(X.shape[1])]

    # Fit regression model
    print("Fitting Random Forest regression model...")
    result = fit_regression(X, y, model="random_forest")
    
    # Print metrics
    print("\nModel Performance:")
    for name, value in result["metrics"].items():
        print(f"  {name}: {value:.4f}")
    
    # Save report
    report_path = save_report(
        result, X, y, 
        task_type="regression",
        feature_names=feature_names,
        output_path="regression_report.html"
    )
    print(f"\nReport saved to: {report_path}")


def classification_example():
    """Demonstrate classification workflow."""
    print("\n=== Classification Example ===")
    
    # Load Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Fit classification model
    print("Fitting Random Forest classification model...")
    result = fit_classification(X, y, model="random_forest")
    
    # Print metrics
    print("\nModel Performance:")
    for name, value in result["metrics"].items():
        print(f"  {name}: {value:.4f}")
    
    # Save report
    report_path = save_report(
        result, X, y, 
        task_type="classification",
        feature_names=iris.feature_names,
        output_path="classification_report.html"
    )
    print(f"\nReport saved to: {report_path}")


def clustering_example():
    """Demonstrate clustering workflow."""
    print("\n=== Clustering Example ===")
    
    # Create synthetic clustering data
    X, y_true = make_blobs(
        n_samples=300, 
        centers=4, 
        cluster_std=0.60, 
        random_state=42
    )
    
    # Fit clustering model
    print("Fitting K-Means clustering model...")
    result = fit_clustering(X, model="kmeans", n_clusters=4)
    
    # Print metrics
    print("\nModel Performance:")
    for name, value in result["metrics"].items():
        print(f"  {name}: {value:.4f}")
    
    # Save report
    report_path = save_report(
        result, X, 
        task_type="clustering",
        feature_names=["Feature 1", "Feature 2"],
        output_path="clustering_report.html"
    )
    print(f"\nReport saved to: {report_path}")


if __name__ == "__main__":
    print("EnginML - Example Usage")
    print("========================")
    
    # Run examples
    regression_example()
    classification_example()
    clustering_example()
    
    print("\nAll examples completed. Check the generated HTML reports.")
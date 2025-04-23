#!/bin/bash
# Example commands for using EnginML from the command line

# Make sure the package is installed
# pip install -e ..

# Example 1: Regression with sample data
echo "Running regression example..."
enginml sample_data.csv --task regression --target target --output regression_report.html

# Example 2: Create a classification dataset and run classification
echo "\nCreating classification sample data..."
python -c "
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

# Create synthetic classification data
X, y = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=42)

# Create DataFrame
df = pd.DataFrame(X, columns=['feature1', 'feature2', 'feature3', 'feature4'])
df['target'] = y

# Save to CSV
df.to_csv('classification_sample.csv', index=False)
print('Created classification_sample.csv')
"

echo "Running classification example..."
enginml classification_sample.csv --task classification --target target --output classification_report.html

# Example 3: Clustering (using all features in the sample data)
echo "\nRunning clustering example..."
enginml sample_data.csv --task clustering --n-clusters 3 --output clustering_report.html

echo "\nAll examples completed. Check the generated HTML reports."
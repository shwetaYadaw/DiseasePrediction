"""
Smart Health Disease Prediction Model Training Script
Trains a Random Forest model on the medical dataset to predict Diabetes
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle
import warnings

warnings.filterwarnings('ignore')

# Load the dataset
print("Loading dataset...")
df = pd.read_csv('Testing.csv')

print(f"Dataset shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(f"Unique diseases: {df['prognosis'].unique()}")

# Get only Diabetes data along with non-Diabetes samples for balanced training
print("\nPreparing data for Diabetes prediction...")

# Create binary classification: Diabetes vs Not Diabetes
y = (df['prognosis'] == 'Diabetes ').astype(int)

# Get feature columns (all except prognosis)
X = df.drop('prognosis', axis=1)

print(f"Features shape: {X.shape}")
print(f"Diabetes cases: {y.sum()}")
print(f"Non-Diabetes cases: {(y == 0).sum()}")
print(f"Feature columns: {X.columns.tolist()}")

# Split the data - handle small datasets
# For small datasets or imbalanced classes, don't use stratification
if len(y) > 10 and min(y.sum(), (y == 0).sum()) >= 2:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
else:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

print(f"\nTraining data: {X_train.shape}")
print(f"Testing data: {X_test.shape}")

# Train Random Forest model
print("\nTraining Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
    class_weight='balanced'
)

model.fit(X_train, y_train)

# Evaluate the model
train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

print(f"\nModel Performance:")
print(f"Training Accuracy: {train_score:.4f}")
print(f"Testing Accuracy: {test_score:.4f}")

# Get feature importance
feature_importance = pd.DataFrame({
    'feature': X.columns,
    'importance': model.feature_importances_
}).sort_values('importance', ascending=False)

print(f"\nTop 15 Important Features:")
print(feature_importance.head(15).to_string(index=False))

# Save the model
model_path = 'models/diabetes_model.pkl'
print(f"\nSaving model to {model_path}...")
with open(model_path, 'wb') as f:
    pickle.dump(model, f)

# Save feature columns for later use
features_path = 'models/feature_columns.pkl'
with open(features_path, 'wb') as f:
    pickle.dump(X.columns.tolist(), f)

print("✓ Model and features saved successfully!")
print("\nReady to use in Flask app!")

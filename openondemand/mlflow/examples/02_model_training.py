# MLflow Model Training Example
# Complete workflow with scikit-learn

import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.datasets import make_classification

print("MLflow Model Training Example")
print("==============================\n")

# Set tracking URI
TRACKING_URI = "http://localhost:5000"  # Replace with actual URI
mlflow.set_tracking_uri(TRACKING_URI)

# Create experiment
mlflow.set_experiment("model-training-demo")

# Generate sample data
print("Generating sample dataset...")
X, y = make_classification(
    n_samples=1000,
    n_features=20,
    n_informative=15,
    n_redundant=5,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}\n")

# Train model with MLflow tracking
print("Training Random Forest model...")

with mlflow.start_run(run_name="random-forest-baseline"):
    
    # Model hyperparameters
    n_estimators = 100
    max_depth = 10
    min_samples_split = 5
    
    # Log parameters
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("min_samples_split", min_samples_split)
    mlflow.log_param("n_features", X_train.shape[1])
    mlflow.log_param("n_samples", X_train.shape[0])
    
    # Train model
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    # Calculate metrics
    train_accuracy = accuracy_score(y_train, y_pred_train)
    test_accuracy = accuracy_score(y_test, y_pred_test)
    precision = precision_score(y_test, y_pred_test)
    recall = recall_score(y_test, y_pred_test)
    f1 = f1_score(y_test, y_pred_test)
    
    # Log metrics
    mlflow.log_metric("train_accuracy", train_accuracy)
    mlflow.log_metric("test_accuracy", test_accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)
    
    print(f"Training Accuracy: {train_accuracy:.4f}")
    print(f"Test Accuracy: {test_accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}\n")
    
    # Log the model
    print("Logging model...")
    mlflow.sklearn.log_model(
        model,
        "random-forest-model",
        registered_model_name="RandomForestClassifier"
    )
    
    # Log feature importance as artifact
    import matplotlib.pyplot as plt
    
    feature_importance = model.feature_importances_
    indices = np.argsort(feature_importance)[::-1][:10]
    
    plt.figure(figsize=(10, 6))
    plt.bar(range(10), feature_importance[indices])
    plt.title('Top 10 Feature Importances')
    plt.xlabel('Feature Index')
    plt.ylabel('Importance')
    plt.savefig('feature_importance.png')
    plt.close()
    
    mlflow.log_artifact('feature_importance.png')
    
    print("Model training complete!")
    print(f"View results: {TRACKING_URI}")

print("\nTraining complete! Check MLflow UI for details.")

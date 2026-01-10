# Basic MLflow Tracking Example
# Demonstrates fundamental MLflow operations

import mlflow
import numpy as np
from datetime import datetime

print("MLflow Basic Tracking Example")
print("==============================\n")

# Set tracking URI (replace with your MLflow server)
# Find this in your MLflow session's connection.yml
TRACKING_URI = "http://localhost:5000"  # Replace with actual URI
mlflow.set_tracking_uri(TRACKING_URI)

print(f"Tracking URI: {mlflow.get_tracking_uri()}")
print(f"MLflow version: {mlflow.__version__}\n")

# Create or set experiment
experiment_name = "basic-tracking-demo"
mlflow.set_experiment(experiment_name)
print(f"Experiment: {experiment_name}\n")

# Start a run
with mlflow.start_run() as run:
    print(f"Run ID: {run.info.run_id}")
    print(f"Run Name: {run.info.run_name}\n")
    
    # Log parameters
    print("Logging parameters...")
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    mlflow.log_param("epochs", 10)
    mlflow.log_param("optimizer", "adam")
    
    # Log metrics
    print("Logging metrics...")
    for epoch in range(10):
        # Simulate training metrics
        train_loss = 1.0 / (epoch + 1) + np.random.rand() * 0.1
        val_loss = 1.2 / (epoch + 1) + np.random.rand() * 0.15
        accuracy = 0.5 + (epoch / 10) * 0.4 + np.random.rand() * 0.05
        
        mlflow.log_metric("train_loss", train_loss, step=epoch)
        mlflow.log_metric("val_loss", val_loss, step=epoch)
        mlflow.log_metric("accuracy", accuracy, step=epoch)
    
    # Log tags
    print("Logging tags...")
    mlflow.set_tag("model_type", "neural_network")
    mlflow.set_tag("framework", "example")
    mlflow.set_tag("date", datetime.now().strftime("%Y-%m-%d"))
    
    # Log a simple artifact (text file)
    print("Logging artifact...")
    with open("model_summary.txt", "w") as f:
        f.write("Model: Simple Neural Network\n")
        f.write("Parameters: 1000\n")
        f.write("Training completed successfully\n")
    
    mlflow.log_artifact("model_summary.txt")
    
    print(f"\nRun completed!")
    print(f"View in MLflow UI: {TRACKING_URI}")

print("\n" + "="*60)
print("Check the MLflow UI to see your logged experiment!")
print("="*60)

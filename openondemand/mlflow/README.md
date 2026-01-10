# MLflow Examples

Examples for MLflow experiment tracking on KENET HPC.

## About MLflow

MLflow is an open-source platform for managing the machine learning lifecycle, including experimentation, reproducibility, and deployment.

## Directory Structure

- `examples/` - Basic MLflow tracking examples
- `workflows/` - Complete ML workflows with MLflow integration

## Requirements

- MLflow 2.x
- Python 3.9+
- scikit-learn, TensorFlow, or PyTorch
- Running MLflow tracking server from Open OnDemand

## Getting Started

1. Launch MLflow from Open OnDemand
2. Note the tracking URI from connection.yml
3. Launch JupyterLab or VS Code
4. Run examples, substituting correct tracking URI

## Basic Usage
```python
import mlflow

# Set tracking URI
mlflow.set_tracking_uri('http://hostname:port')

# Create experiment
mlflow.set_experiment('my-experiment')

# Log parameters and metrics
with mlflow.start_run():
    mlflow.log_param('alpha', 0.5)
    mlflow.log_metric('rmse', 0.85)
```

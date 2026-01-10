# TensorBoard Examples

Examples for TensorBoard visualization on KENET HPC.

## About TensorBoard

TensorBoard is TensorFlow's visualization toolkit for understanding, debugging, and optimizing machine learning experiments.

## Directory Structure

- `examples/` - Basic TensorBoard logging examples
- `workflows/` - Complete workflows with comprehensive visualization

## Requirements

- TensorBoard 2.x
- TensorFlow 2.x or PyTorch 1.x+
- Running TensorBoard server from Open OnDemand

## Getting Started

1. Run training code that generates TensorBoard logs
2. Launch TensorBoard from Open OnDemand pointing to log directory
3. View visualizations in web interface

## Basic Usage

### TensorFlow
```python
from tensorflow.keras.callbacks import TensorBoard

callback = TensorBoard(log_dir='./logs')
model.fit(X, y, callbacks=[callback])
```

### PyTorch
```python
from torch.utils.tensorboard import SummaryWriter

writer = SummaryWriter('logs/experiment1')
writer.add_scalar('Loss/train', loss, epoch)
writer.close()
```

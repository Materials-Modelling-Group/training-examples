# TensorBoard with PyTorch Example
# Manual logging with SummaryWriter

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
import numpy as np

print("TensorBoard PyTorch Logging")
print("============================\n")

# Create log directory
log_dir = f"logs/pytorch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
writer = SummaryWriter(log_dir)
print(f"Log directory: {log_dir}\n")

# Simple neural network
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(20, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, 1)
        self.dropout = nn.Dropout(0.2)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.dropout(x)
        x = torch.relu(self.fc2(x))
        x = self.dropout(x)
        x = torch.sigmoid(self.fc3(x))
        return x

# Initialize
model = SimpleNet()
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Log model graph
print("Logging model graph...")
dummy_input = torch.randn(1, 20)
writer.add_graph(model, dummy_input)

# Generate data
X_train = torch.randn(1000, 20)
y_train = torch.randint(0, 2, (1000, 1)).float()
X_val = torch.randn(200, 20)
y_val = torch.randint(0, 2, (200, 1)).float()

# Training loop
print("\nTraining model...")
print("="*60)

n_epochs = 20
batch_size = 32

for epoch in range(n_epochs):
    # Training
    model.train()
    train_loss = 0.0
    
    for i in range(0, len(X_train), batch_size):
        batch_X = X_train[i:i+batch_size]
        batch_y = y_train[i:i+batch_size]
        
        optimizer.zero_grad()
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
        
        train_loss += loss.item()
    
    train_loss /= (len(X_train) / batch_size)
    
    # Validation
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_val)
        val_loss = criterion(val_outputs, y_val).item()
        
        val_pred = (val_outputs > 0.5).float()
        val_acc = (val_pred == y_val).float().mean().item()
    
    # Log metrics
    writer.add_scalar('Loss/train', train_loss, epoch)
    writer.add_scalar('Loss/validation', val_loss, epoch)
    writer.add_scalar('Accuracy/validation', val_acc, epoch)
    
    # Log histograms of weights
    for name, param in model.named_parameters():
        writer.add_histogram(name, param, epoch)
        if param.grad is not None:
            writer.add_histogram(f'{name}.grad', param.grad, epoch)
    
    print(f"Epoch {epoch+1}/{n_epochs} - "
          f"Train Loss: {train_loss:.4f}, "
          f"Val Loss: {val_loss:.4f}, "
          f"Val Acc: {val_acc:.4f}")

# Close writer
writer.close()

print("\n" + "="*60)
print("Training complete!")
print(f"\nLogs saved to: {log_dir}")
print("\nLaunch TensorBoard from Open OnDemand to visualize results")

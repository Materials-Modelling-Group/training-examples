# TensorBoard with TensorFlow Example
# Basic logging setup

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import TensorBoard
import numpy as np
from datetime import datetime

print("TensorBoard TensorFlow Logging")
print("================================\n")

# Create log directory
log_dir = f"logs/tf_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
print(f"Log directory: {log_dir}\n")

# Generate sample data
print("Generating sample data...")
X_train = np.random.rand(1000, 20)
y_train = np.random.randint(0, 2, 1000)
X_val = np.random.rand(200, 20)
y_val = np.random.randint(0, 2, 200)

# Create model
print("Creating model...")
model = keras.Sequential([
    keras.layers.Dense(64, activation='relu', input_shape=(20,)),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(32, activation='relu'),
    keras.layers.Dropout(0.2),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

print(model.summary())

# Create TensorBoard callback
tensorboard_callback = TensorBoard(
    log_dir=log_dir,
    histogram_freq=1,        # Log weight histograms every epoch
    write_graph=True,        # Log model graph
    write_images=True,       # Log model weights as images
    update_freq='epoch',     # Log metrics after each epoch
    profile_batch='10,20'    # Profile batches 10-20
)

# Train model
print("\nTraining model...")
print("="*60)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=20,
    batch_size=32,
    callbacks=[tensorboard_callback],
    verbose=1
)

print("\n" + "="*60)
print("Training complete!")
print(f"\nLogs saved to: {log_dir}")
print("\nTo view in TensorBoard:")
print(f"  tensorboard --logdir={log_dir}")
print("\nOr launch TensorBoard from Open OnDemand")

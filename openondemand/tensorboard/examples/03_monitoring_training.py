# Comprehensive Training Monitoring with TensorBoard
# Tracks multiple metrics and creates visualizations

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.callbacks import TensorBoard, LearningRateScheduler
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import io

print("Comprehensive TensorBoard Monitoring")
print("=====================================\n")

# Log directory
log_dir = f"logs/monitoring_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
print(f"Log directory: {log_dir}\n")

# Custom callback for additional logging
class CustomTensorBoard(keras.callbacks.Callback):
    def __init__(self, log_dir):
        super().__init__()
        self.writer = tf.summary.create_file_writer(log_dir)
        
    def on_epoch_end(self, epoch, logs=None):
        with self.writer.as_default():
            # Log learning rate
            lr = self.model.optimizer.learning_rate
            if isinstance(lr, tf.keras.optimizers.schedules.LearningRateSchedule):
                lr = lr(self.model.optimizer.iterations)
            tf.summary.scalar('learning_rate', lr, step=epoch)
            
            # Log gradient norms
            gradients = []
            for layer in self.model.layers:
                if hasattr(layer, 'kernel'):
                    gradients.append(tf.norm(layer.kernel))
            
            if gradients:
                avg_grad = tf.reduce_mean(gradients)
                tf.summary.scalar('avg_gradient_norm', avg_grad, step=epoch)
        
        self.writer.flush()

# Generate data
X_train = np.random.rand(2000, 20)
y_train = np.random.randint(0, 3, 2000)
X_val = np.random.rand(500, 20)
y_val = np.random.randint(0, 3, 500)

# Model
model = keras.Sequential([
    keras.layers.Dense(128, activation='relu', input_shape=(20,)),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(3, activation='softmax')
])

# Learning rate schedule
def lr_schedule(epoch):
    return 0.001 * (0.95 ** epoch)

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy', keras.metrics.TopKCategoricalAccuracy(k=2, name='top2_acc')]
)

# Callbacks
callbacks = [
    TensorBoard(
        log_dir=log_dir,
        histogram_freq=1,
        write_graph=True,
        update_freq='epoch'
    ),
    CustomTensorBoard(log_dir),
    LearningRateScheduler(lr_schedule)
]

# Train
print("Training model...")
print("="*60)

history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=30,
    batch_size=64,
    callbacks=callbacks,
    verbose=1
)

print("\n" + "="*60)
print("Training complete!")
print(f"\nView comprehensive metrics in TensorBoard")
print(f"Log directory: {log_dir}")

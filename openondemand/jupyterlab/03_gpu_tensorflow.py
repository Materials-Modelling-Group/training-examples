# Using GPU with TensorFlow

import tensorflow as tf
import numpy as np

# Check GPU availability
print("TensorFlow version:", tf.__version__)
print("GPUs Available:", len(tf.config.list_physical_devices('GPU')))
print("GPU Details:")
for gpu in tf.config.list_physical_devices('GPU'):
    print(f"  {gpu}")

# Create simple neural network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile model (will use GPU automatically if available)
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Generate dummy data
X_train = np.random.rand(1000, 10)
y_train = np.random.randint(0, 10, 1000)

# Train model
print("\nTraining model (using GPU if available)...")
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

print("\nTraining complete!")

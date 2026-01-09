# Basic plotting example
# Press Shift+Enter to run each cell

import pandas as pd
import matplotlib.pyplot as plt

# Create sample data
data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

# Create plot
plt.figure(figsize=(10, 6))
plt.plot(data['x'], data['y'], marker='o')
plt.title('Sample Plot on KENET HPC')
plt.xlabel('X values')
plt.ylabel('Y values')
plt.grid(True)
plt.show()

# Display data
print(data)

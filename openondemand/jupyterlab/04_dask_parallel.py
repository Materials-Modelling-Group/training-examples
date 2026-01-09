# Parallel processing with Dask

import dask.dataframe as dd
import dask
import pandas as pd

# Read large dataset with Dask (parallel processing)
print("Reading large dataset with Dask...")
ddf = dd.read_csv('/scratch/username/large_*.csv')

# Display basic info
print(f"Number of partitions: {ddf.npartitions}")
print(f"Columns: {ddf.columns.tolist()}")

# Perform grouped aggregation (computed in parallel)
print("\nPerforming grouped aggregation...")
result = ddf.groupby('category').agg({
    'value': ['sum', 'mean', 'count']
}).compute()

print(result)

# Filter and process
filtered = ddf[ddf['value'] > 100]
processed = filtered.groupby('date').sum().compute()

# Write results
processed.to_csv('/scratch/username/results.csv')
print("\nResults saved to /scratch/username/results.csv")

# Check cluster info
print(f"\nDask using {dask.system.CPU_COUNT} cores")

# Loading data from cluster storage

import pandas as pd

# Read CSV from your home directory
df = pd.read_csv('/home/username/data/dataset.csv')
print("Data from home directory:")
print(df.head())
print(f"Shape: {df.shape}")

# Read from scratch directory (faster for large files)
df_large = pd.read_csv('/scratch/username/bigdata.csv')
print("\nData from scratch directory:")
print(df_large.head())

# Read with specific options
df_custom = pd.read_csv(
    '/home/username/data/file.csv',
    sep=',',
    header=0,
    na_values=['NA', 'missing']
)

# Read multiple files
import glob
files = glob.glob('/scratch/username/data_*.csv')
df_combined = pd.concat([pd.read_csv(f) for f in files])
print(f"\nCombined {len(files)} files")

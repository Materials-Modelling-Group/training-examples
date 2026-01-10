# Basic PSPP Analysis from JupyterLab
# Demonstrates running PSPP commands from Python

import subprocess
import tempfile
import os

print("PSPP Basic Analysis Example")
print("===========================\n")

# Sample data as CSV
data_csv = """id,group,score
1,A,85
2,A,92
3,A,78
4,B,88
5,B,95
6,B,91
7,C,72
8,C,79
9,C,68
"""

# Save data to temporary file
with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
    f.write(data_csv)
    data_file = f.name

print(f"Created temporary data file: {data_file}\n")

# PSPP syntax for analysis
pspp_syntax = f"""
* Load data from CSV
DATA LIST FILE='{data_file}' free (',')
/id group (A1) score.

* Display data
LIST.

* Descriptive statistics
DESCRIPTIVES VARIABLES=score
/STATISTICS=MEAN STDDEV MIN MAX.

* Frequency table for groups
FREQUENCIES VARIABLES=group.

* Group statistics
MEANS TABLES=score BY group
/CELLS=MEAN STDDEV COUNT.
"""

print("PSPP Syntax:")
print("-" * 40)
print(pspp_syntax)
print("-" * 40)
print()

# Save syntax to temporary file
with tempfile.NamedTemporaryFile(mode='w', suffix='.sps', delete=False) as f:
    f.write(pspp_syntax)
    syntax_file = f.name

print(f"Created temporary syntax file: {syntax_file}\n")

# Run PSPP
print("Running PSPP...")
print("=" * 60)

try:
    result = subprocess.run(
        ['pspp', syntax_file],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    if result.returncode == 0:
        print("PSPP Output:")
        print(result.stdout)
    else:
        print("PSPP Error:")
        print(result.stderr)
        
except FileNotFoundError:
    print("ERROR: PSPP not found!")
    print("PSPP may not be installed or not in PATH")
    print("\nAlternative: Use Python for statistics")
    
    # Show Python alternative
    import pandas as pd
    import numpy as np
    
    # Read data
    df = pd.read_csv(data_file)
    
    print("\nPython Alternative:")
    print("-" * 60)
    print("\nData:")
    print(df)
    
    print("\nDescriptive Statistics:")
    print(df['score'].describe())
    
    print("\nGroup Statistics:")
    print(df.groupby('group')['score'].agg(['mean', 'std', 'count']))

except subprocess.TimeoutExpired:
    print("ERROR: PSPP timed out")

finally:
    # Clean up temporary files
    os.unlink(data_file)
    os.unlink(syntax_file)
    print("\nTemporary files cleaned up")

print("\n" + "=" * 60)
print("Analysis complete!")

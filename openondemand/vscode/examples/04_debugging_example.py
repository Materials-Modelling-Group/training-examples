#!/usr/bin/env python3
"""
Debugging example for VS Code
Demonstrates common debugging scenarios

To debug:
1. Set breakpoints by clicking in the left margin
2. Press F5 or Run > Start Debugging
3. Use the debug toolbar to step through code
"""

import numpy as np
import pandas as pd

def calculate_statistics(data):
    """Calculate basic statistics for a dataset"""
    # Set breakpoint here to inspect data
    mean_val = np.mean(data)
    median_val = np.median(data)
    std_val = np.std(data)
    
    stats = {
        'mean': mean_val,
        'median': median_val,
        'std': std_val,
        'min': np.min(data),
        'max': np.max(data)
    }
    
    return stats

def process_dataframe(df):
    """Process a dataframe with debugging examples"""
    # Breakpoint: inspect dataframe structure
    print(f"Processing {len(df)} rows")
    
    # Example of conditional breakpoint
    # Right-click breakpoint > Edit Breakpoint > Add condition
    for idx, row in df.iterrows():
        value = row['value']
        
        # Set conditional breakpoint here: idx == 5
        if value < 0:
            print(f"Negative value at index {idx}: {value}")
    
    # Calculate grouped statistics
    grouped = df.groupby('category').agg({
        'value': ['mean', 'sum', 'count']
    })
    
    return grouped

def buggy_function(n):
    """Function with intentional bugs for debugging practice"""
    results = []
    
    for i in range(n):
        # Bug 1: Division by zero when i == 5
        result = 100 / (i - 5)
        results.append(result)
    
    return results

def main():
    print("=== Debugging Examples ===\n")
    
    # Example 1: Simple statistics
    data = np.random.randn(100)
    stats = calculate_statistics(data)
    print("Statistics:", stats)
    
    # Example 2: DataFrame processing
    df = pd.DataFrame({
        'category': ['A', 'B', 'A', 'B', 'A'] * 20,
        'value': np.random.randn(100)
    })
    
    grouped = process_dataframe(df)
    print("\nGrouped results:")
    print(grouped)
    
    # Example 3: Debug the buggy function
    # Uncomment to practice debugging
    # try:
    #     results = buggy_function(10)
    # except ZeroDivisionError as e:
    #     print(f"Error: {e}")
    #     # Set breakpoint in buggy_function to find the issue
    
    print("\n=== Debugging Complete ===")

if __name__ == "__main__":
    main()

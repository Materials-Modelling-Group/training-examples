#!/usr/bin/env python3
"""
Complete data analysis workflow script
Demonstrates proper structure, error handling, and logging
"""

import sys
import logging
from pathlib import Path
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(f'analysis_{datetime.now():%Y%m%d_%H%M%S}.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def load_data(filepath):
    """Load data with error handling"""
    try:
        logger.info(f"Loading data from {filepath}")
        df = pd.read_csv(filepath)
        logger.info(f"Successfully loaded {len(df)} rows, {len(df.columns)} columns")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {filepath}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        logger.error(f"File is empty: {filepath}")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error loading file: {e}")
        sys.exit(1)

def validate_data(df, required_columns):
    """Validate dataframe has required columns"""
    logger.info("Validating data structure")
    
    missing_cols = set(required_columns) - set(df.columns)
    if missing_cols:
        logger.error(f"Missing required columns: {missing_cols}")
        return False
    
    logger.info("Data validation passed")
    return True

def clean_data(df):
    """Clean and preprocess data"""
    logger.info("Starting data cleaning")
    
    initial_rows = len(df)
    
    # Remove duplicates
    df = df.drop_duplicates()
    logger.info(f"Removed {initial_rows - len(df)} duplicate rows")
    
    # Handle missing values
    missing_before = df.isnull().sum().sum()
    df = df.fillna(df.median(numeric_only=True))
    logger.info(f"Filled {missing_before} missing values")
    
    return df

def analyze_data(df):
    """Perform statistical analysis"""
    logger.info("Performing statistical analysis")
    
    results = {}
    
    # Basic statistics
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        results[col] = {
            'mean': df[col].mean(),
            'median': df[col].median(),
            'std': df[col].std(),
            'min': df[col].min(),
            'max': df[col].max()
        }
        logger.info(f"{col}: mean={results[col]['mean']:.2f}, std={results[col]['std']:.2f}")
    
    return results

def create_visualizations(df, output_dir):
    """Create and save visualizations"""
    logger.info("Creating visualizations")
    
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Plot 1: Distribution
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    n_cols = len(numeric_cols)
    
    fig, axes = plt.subplots(1, min(n_cols, 3), figsize=(15, 4))
    if n_cols == 1:
        axes = [axes]
    
    for idx, col in enumerate(numeric_cols[:3]):
        axes[idx].hist(df[col], bins=30, edgecolor='black')
        axes[idx].set_title(f'Distribution of {col}')
        axes[idx].set_xlabel(col)
        axes[idx].set_ylabel('Frequency')
    
    plt.tight_layout()
    plot_path = output_dir / 'distributions.png'
    plt.savefig(plot_path, dpi=300)
    logger.info(f"Saved plot to {plot_path}")
    plt.close()

def save_results(df, results, output_dir):
    """Save processed data and results"""
    logger.info("Saving results")
    
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Save cleaned data
    data_path = output_dir / 'cleaned_data.csv'
    df.to_csv(data_path, index=False)
    logger.info(f"Saved cleaned data to {data_path}")
    
    # Save statistics
    stats_df = pd.DataFrame(results).T
    stats_path = output_dir / 'statistics.csv'
    stats_df.to_csv(stats_path)
    logger.info(f"Saved statistics to {stats_path}")

def main():
    """Main analysis workflow"""
    logger.info("=" * 60)
    logger.info("Starting data analysis workflow")
    logger.info("=" * 60)
    
    # Configuration
    input_file = Path.home() / 'data' / 'input.csv'
    output_dir = Path('results')
    required_columns = ['date', 'value']  # Adjust as needed
    
    # Load data
    df = load_data(input_file)
    
    # Validate
    if not validate_data(df, required_columns):
        sys.exit(1)
    
    # Clean
    df = clean_data(df)
    
    # Analyze
    results = analyze_data(df)
    
    # Visualize
    create_visualizations(df, output_dir)
    
    # Save
    save_results(df, results, output_dir)
    
    logger.info("=" * 60)
    logger.info("Analysis complete!")
    logger.info("=" * 60)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception("Unexpected error occurred")
        sys.exit(1)

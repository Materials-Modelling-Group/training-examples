# PSPP in JupyterLab Examples

Examples for using PSPP statistical analysis software within JupyterLab on KENET HPC.

## About PSPP

PSPP is a free and open-source statistical analysis program, designed as a free alternative to IBM SPSS Statistics. It can perform descriptive statistics, t-tests, ANOVA, linear regression, logistic regression, reliability analysis, factor analysis, and more.

## Directory Structure

- `examples/` - Basic PSPP examples and Python alternatives
- `workflows/` - Complete analysis workflows combining PSPP and Python

## Requirements

- JupyterLab environment
- PSPP installed and accessible from command line
- Python packages: pandas, numpy, scipy, matplotlib, seaborn

## Two Approaches

### Approach 1: PSPP via subprocess
Run PSPP syntax from Python notebooks using subprocess module.

### Approach 2: Pure Python
Use scipy.stats, statsmodels, and pandas for similar analyses.

## Getting Started

1. Launch JupyterLab from Open OnDemand
2. Create new Python notebook
3. Try examples in order, starting with `01_basic_analysis.py`

## Note on Syntax Files

Files with `.sps` extension contain PSPP syntax. These are run from Python using subprocess or can be executed directly with:
```bash
pspp script.sps
```

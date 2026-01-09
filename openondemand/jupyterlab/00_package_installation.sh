#!/bin/bash
# Installing Python packages in JupyterLab
# Use this in a notebook cell with ! prefix

# Install single package
!pip install --user seaborn

# Install multiple packages
!pip install --user scikit-learn pandas matplotlib

# Using %pip magic (alternative method)
%pip install --user packagename

# After installation, restart the kernel:
# Kernel → Restart Kernel

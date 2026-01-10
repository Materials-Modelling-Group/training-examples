#!/usr/bin/env python3
"""
Simple Python script to test VS Code on KENET HPC cluster
This demonstrates basic Python execution and cluster information
"""

import os
import sys
import socket
import platform
from datetime import datetime

def main():
    print("=" * 60)
    print("Hello from KENET HPC Cluster!")
    print("=" * 60)
    
    # System information
    print(f"\nSystem Information:")
    print(f"  Hostname: {socket.gethostname()}")
    print(f"  Platform: {platform.platform()}")
    print(f"  Python Version: {sys.version}")
    print(f"  Python Executable: {sys.executable}")
    
    # User and environment
    print(f"\nUser Information:")
    print(f"  Username: {os.getenv('USER')}")
    print(f"  Home Directory: {os.getenv('HOME')}")
    print(f"  Current Directory: {os.getcwd()}")
    
    # Date and time
    print(f"\nCurrent Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Check for common libraries
    print(f"\nChecking installed packages:")
    try:
        import numpy
        print(f"   NumPy {numpy.__version__}")
    except ImportError:
        print(f"   NumPy not installed")
    
    try:
        import pandas
        print(f"  ✓ Pandas {pandas.__version__}")
    except ImportError:
        print(f"   Pandas not installed")
    
    try:
        import matplotlib
        print(f"   Matplotlib {matplotlib.__version__}")
    except ImportError:
        print(f"   Matplotlib not installed")
    
    print("\n" + "=" * 60)
    print("Script completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()

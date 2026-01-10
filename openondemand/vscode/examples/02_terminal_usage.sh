#!/bin/bash
# Common terminal commands for HPC cluster usage
# Run these in VS Code's integrated terminal

# Show current directory
echo "Current directory:"
pwd

# List files with details
echo -e "\nFiles in current directory:"
ls -lah

# Check disk usage
echo -e "\nDisk usage in home directory:"
du -sh ~/

# Check disk quota
echo -e "\nDisk quota:"
quota -s

# Show loaded modules
echo -e "\nCurrently loaded modules:"
module list

# Show available modules
echo -e "\nAvailable modules (first 20):"
module avail 2>&1 | head -20

# Check Slurm job status
echo -e "\nYour running jobs:"
squeue -u $USER

# System information
echo -e "\nNode information:"
hostname
cat /proc/cpuinfo | grep "model name" | head -1
cat /proc/meminfo | grep MemTotal

# Python version
echo -e "\nPython version:"
python --version

# Useful aliases you can add to ~/.bashrc
cat << 'EOF'

Useful aliases to add to your ~/.bashrc:
----------------------------------------
alias ll='ls -lah'
alias jobs='squeue -u $USER'
alias myquota='quota -s'
alias scratch='cd /scratch/$USER'
EOF

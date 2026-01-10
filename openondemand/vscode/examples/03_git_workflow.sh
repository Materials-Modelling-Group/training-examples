#!/bin/bash
# Git workflow examples for VS Code on HPC cluster

# === Initial Setup ===

# Configure Git (run once)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default branch name
git config --global init.defaultBranch main

# === Initialize Repository ===

# Create new repository
cd ~/projects/my-research
git init

# Create .gitignore file
cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*.so
.Python

# Data files (don't commit large data)
*.csv
*.h5
*.hdf5
data/

# Results
results/
*.png
*.pdf

# Jupyter
.ipynb_checkpoints/

# VS Code
.vscode/

# Environment
.env
*.secret
EOF

# Add and commit files
git add .
git commit -m "Initial commit"

# === Working with Remote Repository ===

# Add remote (GitHub/GitLab)
git remote add origin git@github.com:username/repo.git

# Push to remote
git push -u origin main

# === SSH Key Setup for Git ===

# Generate SSH key (if you don't have one)
ssh-keygen -t ed25519 -C "your.email@example.com"

# Show public key (add this to GitHub/GitLab)
cat ~/.ssh/id_ed25519.pub

# Test connection
ssh -T git@github.com

# === Common Git Workflow ===

# Check status
git status

# Add files
git add filename.py
git add .  # add all changes

# Commit changes
git commit -m "Descriptive commit message"

# Push to remote
git push

# Pull latest changes
git pull

# === Branching ===

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Merge branch
git merge feature-name

# Delete branch
git branch -d feature-name

# === Viewing History ===

# View commit log
git log
git log --oneline
git log --graph --all --oneline

# View changes
git diff
git diff filename.py

# === Undo Changes ===

# Discard changes in file
git checkout -- filename.py

# Unstage file
git reset HEAD filename.py

# Undo last commit (keep changes)
git reset --soft HEAD~1

# === Tips ===

# Create alias for common commands
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit

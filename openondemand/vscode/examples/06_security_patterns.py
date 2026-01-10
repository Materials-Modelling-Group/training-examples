#!/usr/bin/env python3
"""
Security patterns for handling credentials and sensitive data
Demonstrates best practices for VS Code development
"""

import os
from pathlib import Path

# === BAD: Never do this ===
# API_KEY = "sk-1234567890abcdef"  # NEVER hardcode credentials!
# PASSWORD = "mypassword123"        # NEVER commit passwords!

# === GOOD: Use environment variables ===

def get_api_key():
    """Safely retrieve API key from environment"""
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY environment variable not set")
    return api_key

def get_database_url():
    """Safely retrieve database URL from environment"""
    db_url = os.getenv('DATABASE_URL')
    if not db_url:
        # Provide helpful error message
        raise ValueError(
            "DATABASE_URL not set. "
            "Set it with: export DATABASE_URL='your-url'"
        )
    return db_url

# === GOOD: Use config files (excluded from Git) ===

def load_config():
    """Load configuration from file not in version control"""
    config_file = Path.home() / '.myapp' / 'config.ini'
    
    if not config_file.exists():
        raise FileNotFoundError(
            f"Config file not found at {config_file}\n"
            "Create it with your credentials"
        )
    
    # Read config file
    # (In production, use configparser or similar)
    with open(config_file) as f:
        config = {}
        for line in f:
            if '=' in line:
                key, value = line.strip().split('=', 1)
                config[key] = value
    
    return config

# === Setting up .gitignore ===

GITIGNORE_CONTENT = """
# Credentials and secrets
*.secret
.env
.env.local
config.ini
credentials.json

# API keys
*_key.txt
*_secret.txt

# Database
*.db
*.sqlite

# VS Code
.vscode/
*.code-workspace
"""

def create_gitignore():
    """Create a proper .gitignore file"""
    gitignore_path = Path('.gitignore')
    
    if not gitignore_path.exists():
        gitignore_path.write_text(GITIGNORE_CONTENT)
        print(f"Created .gitignore at {gitignore_path}")
    else:
        print(".gitignore already exists")

# === Example usage ===

def main():
    print("Security Patterns Example\n")
    
    # Example 1: Environment variables
    print("1. Using environment variables:")
    try:
        api_key = get_api_key()
        print(f"   API Key loaded: {api_key[:8]}...")
    except ValueError as e:
        print(f"   Error: {e}")
        print("   Set it with: export API_KEY='your-key'")
    
    # Example 2: Config file
    print("\n2. Using config file:")
    try:
        config = load_config()
        print(f"   Config loaded: {len(config)} settings")
    except FileNotFoundError as e:
        print(f"   {e}")
    
    # Example 3: Create .gitignore
    print("\n3. Creating .gitignore:")
    create_gitignore()
    
    print("\n=== Best Practices ===")
    print(" Store secrets in environment variables")
    print(" Use config files excluded from Git")
    print(" Never commit credentials to version control")
    print(" Use .gitignore to prevent accidental commits")
    print(" Rotate credentials if accidentally exposed")

if __name__ == "__main__":
    main()

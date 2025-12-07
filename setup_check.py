#!/usr/bin/env python
"""
SmartCrop - Quick Setup Guide
This script helps verify and setup your environment
"""

import os
import sys
import subprocess

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required. Current version:", f"{version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor} OK")
    return True

def check_file_exists(filepath):
    """Check if file exists"""
    if os.path.exists(filepath):
        print(f"✓ {filepath} found")
        return True
    print(f"❌ {filepath} NOT found")
    return False

def check_directory_exists(dirpath):
    """Check if directory exists"""
    if os.path.isdir(dirpath):
        print(f"✓ {dirpath}/ exists")
        return True
    print(f"⚠️  {dirpath}/ NOT found")
    return False

def main():
    print("\n" + "="*50)
    print("SmartCrop - Environment Check")
    print("="*50 + "\n")
    
    all_good = True
    
    # Check Python version
    print("1. Checking Python version...")
    if not check_python_version():
        all_good = False
    print()
    
    # Check files
    print("2. Checking required files...")
    files_to_check = [
        'Testing.csv',
        'app.py',
        'train_model.py',
        'requirements.txt',
        'README.md'
    ]
    for file in files_to_check:
        if not check_file_exists(file):
            all_good = False
    print()
    
    # Check directories
    print("3. Checking directories...")
    dirs_to_check = [
        'templates',
        'static',
        'models'
    ]
    for dir in dirs_to_check:
        if not check_directory_exists(dir):
            all_good = False
    print()
    
    # Check template files
    print("4. Checking template files...")
    templates = [
        'templates/index.html',
        'templates/about.html',
        'templates/health_tips.html'
    ]
    for template in templates:
        if not check_file_exists(template):
            all_good = False
    print()
    
    # Check static files
    print("5. Checking static files...")
    statics = [
        'static/style.css',
        'static/script.js'
    ]
    for static in statics:
        if not check_file_exists(static):
            all_good = False
    print()
    
    # Summary
    print("="*50)
    if all_good:
        print("✓ Environment check PASSED!")
        print("\nNext steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Train the model: python train_model.py")
        print("3. Run the app: python app.py")
        print("4. Open browser: http://localhost:5000")
    else:
        print("❌ Some checks failed!")
        print("Please ensure all files and directories are in place.")
    print("="*50 + "\n")
    
    return all_good

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

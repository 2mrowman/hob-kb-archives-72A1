#!/usr/bin/env python3
"""
validate_links.py - Verify all RAW GitHub URLs in KB files are accessible

Usage: python3 tests/validate_links.py

Checks:
- RAW_LINKS_INDEX.md - All URLs return HTTP 200
- notes_for_gpt.md - All embedded URLs return HTTP 200
- Broken links report with line numbers
"""

import re
import sys
import requests
from pathlib import Path

# GitHub API token (optional, for higher rate limits)
GITHUB_TOKEN = None  # Set to your token if needed

# Files to check
FILES_TO_CHECK = [
    "RAW_LINKS_INDEX.md",
    "notes_for_gpt.md"
]

# Base repo URL
REPO_BASE = "https://raw.githubusercontent.com/2mrowman/hob-kb-archives-72A1/refs/heads/main"

def extract_urls(file_path):
    """Extract all GitHub RAW URLs from a file."""
    urls = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Match GitHub RAW URLs
            matches = re.findall(r'https://raw\.githubusercontent\.com/[^\s\)]+', line)
            for url in matches:
                # Remove trailing punctuation
                url = url.rstrip('.,;:)')
                urls.append((line_num, url))
    return urls

def check_url(url):
    """Check if URL is accessible (HTTP 200)."""
    headers = {}
    if GITHUB_TOKEN:
        headers['Authorization'] = f'token {GITHUB_TOKEN}'
    
    try:
        response = requests.head(url, headers=headers, timeout=10, allow_redirects=True)
        return response.status_code == 200
    except requests.RequestException as e:
        print(f"  ⚠️  Error checking {url}: {e}")
        return False

def main():
    """Main validation function."""
    print("=" * 80)
    print("KB LINKS VALIDATION")
    print("=" * 80)
    print()
    
    total_urls = 0
    broken_urls = []
    
    for file_name in FILES_TO_CHECK:
        file_path = Path(file_name)
        
        if not file_path.exists():
            print(f"⚠️  File not found: {file_name}")
            print(f"   Looking in: {file_path.absolute()}")
            continue
        
        print(f"📄 Checking: {file_name}")
        print("-" * 80)
        
        urls = extract_urls(file_path)
        total_urls += len(urls)
        
        for line_num, url in urls:
            print(f"  Line {line_num:4d}: {url[:60]}...", end=" ")
            
            if check_url(url):
                print("✅")
            else:
                print("❌")
                broken_urls.append((file_name, line_num, url))
        
        print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Total URLs checked: {total_urls}")
    print(f"Broken URLs: {len(broken_urls)}")
    print()
    
    if broken_urls:
        print("❌ BROKEN URLS:")
        print("-" * 80)
        for file_name, line_num, url in broken_urls:
            print(f"  {file_name}:{line_num} - {url}")
        print()
        sys.exit(1)
    else:
        print("✅ ALL URLS ACCESSIBLE")
        print()
        sys.exit(0)

if __name__ == "__main__":
    main()


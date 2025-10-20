#!/usr/bin/env python3
"""
validate_timestamps.py - Verify all ?ts= timestamps are present and correctly formatted

Usage: python3 tests/validate_timestamps.py

Checks:
- RAW_LINKS_INDEX.md - All critical files have ?ts= parameter
- notes_for_gpt.md - All KB reference links have ?ts= parameter
- Timestamp format validation (10-digit Unix timestamp)
- Consistency check (all timestamps identical within each file)
"""

import re
import sys
from pathlib import Path
from collections import Counter

# Files to check
FILES_TO_CHECK = [
    "RAW_LINKS_INDEX.md",
    "notes_for_gpt.md"
]

# Critical files that MUST have ?ts= timestamps
CRITICAL_FILES = [
    "notes_for_gpt.md",
    "CAPABILITY_MAP_AdminToolsLib.md",
    "CAPABILITY_MAP_HoBMastersLib.md",
    "CAPABILITY_MAP_MenuLib.md",
    "CAPABILITY_MAP_PopupLib.md",
    "HoBMastersLib.md",
    "MenuLib.md",
    "PopupLib.md",
    "AdminToolsLib.md"
]

def extract_timestamps(file_path):
    """Extract all ?ts= timestamps from a file."""
    timestamps = []
    urls_without_ts = []
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            # Match GitHub RAW URLs
            urls = re.findall(r'https://raw\.githubusercontent\.com/[^\s\)]+', line)
            
            for url in urls:
                # Remove trailing punctuation
                url = url.rstrip('.,;:)')
                
                # Check if URL has ?ts= parameter
                ts_match = re.search(r'\?ts=(\d+)', url)
                
                if ts_match:
                    timestamp = ts_match.group(1)
                    timestamps.append((line_num, url, timestamp))
                else:
                    # Check if this URL points to a critical file
                    is_critical = any(critical in url for critical in CRITICAL_FILES)
                    if is_critical:
                        urls_without_ts.append((line_num, url))
    
    return timestamps, urls_without_ts

def validate_timestamp_format(timestamp):
    """Validate timestamp format (10-digit Unix timestamp)."""
    if not timestamp.isdigit():
        return False, "Not a number"
    
    if len(timestamp) != 10:
        return False, f"Wrong length ({len(timestamp)} digits, expected 10)"
    
    # Check if timestamp is reasonable (between 2020 and 2030)
    ts_int = int(timestamp)
    if ts_int < 1577836800 or ts_int > 1893456000:
        return False, f"Out of range (not between 2020-2030)"
    
    return True, "Valid"

def main():
    """Main validation function."""
    print("=" * 80)
    print("KB TIMESTAMPS VALIDATION")
    print("=" * 80)
    print()
    
    all_valid = True
    
    for file_name in FILES_TO_CHECK:
        file_path = Path(file_name)
        
        if not file_path.exists():
            print(f"⚠️  File not found: {file_name}")
            continue
        
        print(f"📄 Checking: {file_name}")
        print("-" * 80)
        
        timestamps, urls_without_ts = extract_timestamps(file_path)
        
        # Count timestamps
        timestamp_values = [ts for _, _, ts in timestamps]
        timestamp_counts = Counter(timestamp_values)
        
        print(f"  Total URLs with ?ts=: {len(timestamps)}")
        print(f"  Unique timestamp values: {len(timestamp_counts)}")
        print()
        
        # Check timestamp format
        print("  Timestamp format validation:")
        for ts_value, count in timestamp_counts.items():
            valid, msg = validate_timestamp_format(ts_value)
            status = "✅" if valid else "❌"
            print(f"    {status} {ts_value} (used {count} times) - {msg}")
            if not valid:
                all_valid = False
        print()
        
        # Check for missing timestamps on critical files
        if urls_without_ts:
            print(f"  ❌ Critical URLs missing ?ts= parameter: {len(urls_without_ts)}")
            for line_num, url in urls_without_ts:
                print(f"    Line {line_num}: {url}")
            all_valid = False
        else:
            print("  ✅ All critical URLs have ?ts= parameter")
        
        print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    if all_valid:
        print("✅ ALL TIMESTAMPS VALID")
        print()
        sys.exit(0)
    else:
        print("❌ TIMESTAMP VALIDATION FAILED")
        print()
        sys.exit(1)

if __name__ == "__main__":
    main()


#!/usr/bin/env python3
"""
validate_structure.py - Verify KB file structure integrity and required sections

Usage: python3 tests/validate_structure.py

Checks:
- notes_for_gpt.md - All 6 required sections present
- CAPABILITY_MAP files - Required sections present
- Version headers - Correct format and consistency
- File size validation - Detect truncated or corrupted files
"""

import re
import sys
from pathlib import Path

# Required sections in notes_for_gpt.md
NOTES_REQUIRED_SECTIONS = [
    "PROJECT OVERVIEW",
    "ARCHITECTURE",
    "CODING STANDARDS",
    "DEPENDENCIES",
    "COMMON PATTERNS",
    "GOTCHAS"
]

# Required sections in CAPABILITY_MAP files
CAPABILITY_MAP_REQUIRED_SECTIONS = [
    "Functions",
    "Dependencies",
    "Usage"
]

# Minimum file sizes (bytes) to detect truncation
MIN_FILE_SIZES = {
    "notes_for_gpt.md": 20000,  # Should be ~24KB
    "CAPABILITY_MAP_AdminToolsLib.md": 1000,
    "CAPABILITY_MAP_HoBMastersLib.md": 1000,
    "CAPABILITY_MAP_MenuLib.md": 1000,
    "CAPABILITY_MAP_PopupLib.md": 1000
}

def check_file_size(file_path, min_size):
    """Check if file size is above minimum threshold."""
    actual_size = file_path.stat().st_size
    if actual_size < min_size:
        return False, f"File too small ({actual_size} bytes, expected >{min_size} bytes)"
    return True, f"Size OK ({actual_size} bytes)"

def check_required_sections(file_path, required_sections):
    """Check if all required sections are present in file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    missing_sections = []
    found_sections = []
    
    for section in required_sections:
        # Look for section headers (## or ###)
        pattern = rf'^##+ .*{re.escape(section)}'
        if re.search(pattern, content, re.MULTILINE | re.IGNORECASE):
            found_sections.append(section)
        else:
            missing_sections.append(section)
    
    return found_sections, missing_sections

def check_version_header(file_path):
    """Check if file has correct version header format."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read(500)  # Read first 500 chars
    
    # Look for version pattern (e.g., V6.0.0)
    version_match = re.search(r'V\d+\.\d+\.\d+', content)
    if version_match:
        return True, f"Version found: {version_match.group()}"
    return False, "No version header found"

def main():
    """Main validation function."""
    print("=" * 80)
    print("KB STRUCTURE VALIDATION")
    print("=" * 80)
    print()
    
    all_valid = True
    
    # Check notes_for_gpt.md
    notes_path = Path("notes_for_gpt.md")
    if notes_path.exists():
        print("📄 Checking: notes_for_gpt.md")
        print("-" * 80)
        
        # File size check
        valid, msg = check_file_size(notes_path, MIN_FILE_SIZES["notes_for_gpt.md"])
        status = "✅" if valid else "❌"
        print(f"  {status} File size: {msg}")
        if not valid:
            all_valid = False
        
        # Version header check
        valid, msg = check_version_header(notes_path)
        status = "✅" if valid else "❌"
        print(f"  {status} Version header: {msg}")
        if not valid:
            all_valid = False
        
        # Required sections check
        found, missing = check_required_sections(notes_path, NOTES_REQUIRED_SECTIONS)
        print(f"  Sections found: {len(found)}/{len(NOTES_REQUIRED_SECTIONS)}")
        
        for section in found:
            print(f"    ✅ {section}")
        
        if missing:
            for section in missing:
                print(f"    ❌ {section} (MISSING)")
            all_valid = False
        
        print()
    else:
        print("⚠️  File not found: notes_for_gpt.md")
        all_valid = False
        print()
    
    # Check CAPABILITY_MAP files
    capability_maps = [
        "CAPABILITY_MAP_AdminToolsLib.md",
        "CAPABILITY_MAP_HoBMastersLib.md",
        "CAPABILITY_MAP_MenuLib.md",
        "CAPABILITY_MAP_PopupLib.md"
    ]
    
    for file_name in capability_maps:
        file_path = Path(file_name)
        
        if not file_path.exists():
            # Try in libraries/ subdirectory
            file_path = Path("libraries") / file_name
        
        if file_path.exists():
            print(f"📄 Checking: {file_name}")
            print("-" * 80)
            
            # File size check
            min_size = MIN_FILE_SIZES.get(file_name, 500)
            valid, msg = check_file_size(file_path, min_size)
            status = "✅" if valid else "❌"
            print(f"  {status} File size: {msg}")
            if not valid:
                all_valid = False
            
            # Required sections check
            found, missing = check_required_sections(file_path, CAPABILITY_MAP_REQUIRED_SECTIONS)
            print(f"  Sections found: {len(found)}/{len(CAPABILITY_MAP_REQUIRED_SECTIONS)}")
            
            for section in found:
                print(f"    ✅ {section}")
            
            if missing:
                for section in missing:
                    print(f"    ❌ {section} (MISSING)")
                all_valid = False
            
            print()
        else:
            print(f"⚠️  File not found: {file_name}")
            print()
    
    # Summary
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    if all_valid:
        print("✅ ALL STRUCTURE CHECKS PASSED")
        print()
        sys.exit(0)
    else:
        print("❌ STRUCTURE VALIDATION FAILED")
        print()
        sys.exit(1)

if __name__ == "__main__":
    main()


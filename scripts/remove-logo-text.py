#!/usr/bin/env python3
"""Remove 'Best Astaxanthin' text next to logo image since logo contains the text"""

import os
import re
from pathlib import Path

def update_logo_in_file(filepath):
    """Remove text from logo in a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to match logo with image and text
    old_pattern = r'(<div class="logo">\s*<a href="[^"]*" aria-label="Best Astaxanthin Home">\s*<img src="[^"]*" alt="Best Astaxanthin" class="logo-image">)\s*<span>Best Astaxanthin</span>'

    # New logo structure without text span
    new_logo = r'\1'

    # Replace the logo
    updated_content = re.sub(old_pattern, new_logo, content, flags=re.DOTALL)

    if updated_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        return True
    return False

def main():
    """Update all HTML files"""
    updated_count = 0

    # Root directory files
    root_files = Path('.').glob('*.html')
    for filepath in root_files:
        if update_logo_in_file(filepath):
            print(f"Updated: {filepath}")
            updated_count += 1

    # Subdirectory files (reviews, guides, blog)
    for subdir in ['reviews', 'guides', 'blog']:
        subdir_path = Path(subdir)
        if subdir_path.exists():
            for filepath in subdir_path.glob('*.html'):
                if update_logo_in_file(filepath):
                    print(f"Updated: {filepath}")
                    updated_count += 1

    print(f"\nTotal files updated: {updated_count}")

if __name__ == '__main__':
    main()

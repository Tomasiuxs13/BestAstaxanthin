#!/usr/bin/env python3
"""Replace Font Awesome flask icon with actual logo image in all pages"""

import os
import re
from pathlib import Path

def update_logo_in_file(filepath, is_subdir=False):
    """Update logo from icon to image in a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Determine the correct path to logo based on file location
    logo_path = '../assets/images/logo.png' if is_subdir else 'assets/images/logo.png'

    # Pattern to match the current logo structure with icon
    old_pattern = r'<div class="logo">\s*<a href="[^"]*" aria-label="Best Astaxanthin Home">\s*<i class="fas fa-flask"></i>\s*<span>Best Astaxanthin</span>\s*</a>'

    # New logo structure with image
    new_logo = f'''<div class="logo">
                <a href="/" aria-label="Best Astaxanthin Home">
                    <img src="{logo_path}" alt="Best Astaxanthin" class="logo-image">
                    <span>Best Astaxanthin</span>
                </a>'''

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
        if update_logo_in_file(filepath, is_subdir=False):
            print(f"Updated: {filepath}")
            updated_count += 1

    # Subdirectory files (reviews, guides, blog)
    for subdir in ['reviews', 'guides', 'blog']:
        subdir_path = Path(subdir)
        if subdir_path.exists():
            for filepath in subdir_path.glob('*.html'):
                if update_logo_in_file(filepath, is_subdir=True):
                    print(f"Updated: {filepath}")
                    updated_count += 1

    print(f"\nTotal files updated: {updated_count}")

if __name__ == '__main__':
    main()

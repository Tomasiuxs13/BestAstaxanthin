#!/usr/bin/env python3
"""Update all favicon references from .ico to .png"""

import os
from pathlib import Path

def update_favicon_in_file(filepath):
    """Update favicon reference in a single HTML file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace .ico with .png in favicon link
    old_ref = 'href="assets/images/favicon.ico"'
    new_ref = 'href="assets/images/favicon.png"'

    old_ref_relative = 'href="../assets/images/favicon.ico"'
    new_ref_relative = 'href="../assets/images/favicon.png"'

    updated = False
    if old_ref in content:
        content = content.replace(old_ref, new_ref)
        updated = True
    if old_ref_relative in content:
        content = content.replace(old_ref_relative, new_ref_relative)
        updated = True

    if updated:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Update all HTML files"""
    html_files = []

    # Root directory
    html_files.extend(Path('.').glob('*.html'))

    # Subdirectories
    for subdir in ['reviews', 'guides', 'blog']:
        html_files.extend(Path(subdir).glob('*.html'))

    updated_count = 0
    for filepath in html_files:
        if update_favicon_in_file(filepath):
            print(f"Updated: {filepath}")
            updated_count += 1

    print(f"\nTotal files updated: {updated_count}")

if __name__ == '__main__':
    main()

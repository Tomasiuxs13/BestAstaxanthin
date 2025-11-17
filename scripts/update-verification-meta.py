#!/usr/bin/env python3
"""Update fo-verify meta tag content in all HTML files."""

import re
from pathlib import Path

OLD_CONTENT = "567d86b3-91fe-4468-a318-f2cdef453c5e"
NEW_CONTENT = "773efce8-233d-40cf-a46d-3b7205b315e2"

def update_verification_meta(filepath):
    """Update fo-verify meta tag content in HTML file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if fo-verify tag exists
    if 'fo-verify' not in content:
        return False
    
    # Replace the old content with new content
    if OLD_CONTENT in content:
        new_content = content.replace(OLD_CONTENT, NEW_CONTENT)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    
    return False

def main():
    """Update verification meta tag in all HTML files."""
    base_dir = Path('.')
    html_files = list(base_dir.rglob('*.html'))
    
    updated = 0
    skipped = 0
    
    for html_file in html_files:
        try:
            if update_verification_meta(html_file):
                print(f"Updated: {html_file}")
                updated += 1
            else:
                content = html_file.read_text(encoding='utf-8')
                if 'fo-verify' in content:
                    print(f"Already has new content or different format: {html_file}")
                    skipped += 1
        except Exception as e:
            print(f"Error with {html_file}: {e}")
    
    print(f"\nTotal updated: {updated}")
    print(f"Total skipped: {skipped}")

if __name__ == '__main__':
    main()


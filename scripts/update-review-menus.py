#!/usr/bin/env python3
import os
import re

# Define the old dropdown menu HTML (3 items)
old_menu_pattern = r'''<a href="(\.\.\/)?reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="(\.\.\/)?reviews\/sports-research-astaxanthin-review\.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="(\.\.\/)?reviews\/life-extension-astaxanthin-review\.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="(\.\.\/)?reviews\/nutrex-hawaii-bioastin-review\.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                    </ul>'''

# For files in reviews/ directory (no ../ prefix)
new_menu_reviews_dir = '''<a href="../reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                        <li role="none"><a href="microingredients-astaxanthin-review.html" role="menuitem">#4: Microingredients</a></li>
                        <li role="none"><a href="double-wood-astaxanthin-review.html" role="menuitem">#5: Double Wood</a></li>
                        <li role="none"><a href="nutricost-astaxanthin-review.html" role="menuitem">#6: Nutricost</a></li>
                        <li role="none"><a href="vivonu-astaxanthin-review.html" role="menuitem">#7: Vivonu</a></li>
                        <li role="none"><a href="now-foods-astaxanthin-review.html" role="menuitem">#8: NOW Foods</a></li>
                        <li role="none"><a href="naturebell-astaxanthin-review.html" role="menuitem">#9: NatureBell</a></li>
                        <li role="none"><a href="bulksupplements-astaxanthin-review.html" role="menuitem">#10: BulkSupplements</a></li>
                    </ul>'''

# For other files (with reviews/ prefix)
new_menu_other = '''<a href="/reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="reviews/sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="reviews/life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="reviews/nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                        <li role="none"><a href="reviews/microingredients-astaxanthin-review.html" role="menuitem">#4: Microingredients</a></li>
                        <li role="none"><a href="reviews/double-wood-astaxanthin-review.html" role="menuitem">#5: Double Wood</a></li>
                        <li role="none"><a href="reviews/nutricost-astaxanthin-review.html" role="menuitem">#6: Nutricost</a></li>
                        <li role="none"><a href="reviews/vivonu-astaxanthin-review.html" role="menuitem">#7: Vivonu</a></li>
                        <li role="none"><a href="reviews/now-foods-astaxanthin-review.html" role="menuitem">#8: NOW Foods</a></li>
                        <li role="none"><a href="reviews/naturebell-astaxanthin-review.html" role="menuitem">#9: NatureBell</a></li>
                        <li role="none"><a href="reviews/bulksupplements-astaxanthin-review.html" role="menuitem">#10: BulkSupplements</a></li>
                    </ul>'''

# For guides/ directory (with ../reviews/ prefix)
new_menu_guides_dir = '''<a href="../reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="../reviews/sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="../reviews/life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="../reviews/nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                        <li role="none"><a href="../reviews/microingredients-astaxanthin-review.html" role="menuitem">#4: Microingredients</a></li>
                        <li role="none"><a href="../reviews/double-wood-astaxanthin-review.html" role="menuitem">#5: Double Wood</a></li>
                        <li role="none"><a href="../reviews/nutricost-astaxanthin-review.html" role="menuitem">#6: Nutricost</a></li>
                        <li role="none"><a href="../reviews/vivonu-astaxanthin-review.html" role="menuitem">#7: Vivonu</a></li>
                        <li role="none"><a href="../reviews/now-foods-astaxanthin-review.html" role="menuitem">#8: NOW Foods</a></li>
                        <li role="none"><a href="../reviews/naturebell-astaxanthin-review.html" role="menuitem">#9: NatureBell</a></li>
                        <li role="none"><a href="../reviews/bulksupplements-astaxanthin-review.html" role="menuitem">#10: BulkSupplements</a></li>
                    </ul>'''

def update_file(filepath):
    """Update the reviews dropdown menu in a single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # Determine which replacement to use based on file location
        if '/reviews/' in filepath and not filepath.endswith('reviews/index.html'):
            # Review detail pages - use paths without reviews/ prefix
            content = content.replace(
                '''<a href="../reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                    </ul>''',
                new_menu_reviews_dir
            )
        elif '/guides/' in filepath:
            # Guide pages - use paths with ../reviews/ prefix
            content = content.replace(
                '''<a href="../reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="../reviews/sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="../reviews/life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="../reviews/nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                    </ul>''',
                new_menu_guides_dir
            )
        else:
            # Root level and other pages - already updated in index.html
            return False

        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        print(f"Error updating {filepath}: {e}")
        return False

# Find all HTML files
base_dir = '/Users/tomasnorkus/Best Astaxanthin2/BestAstaxanthin'
updated_files = []

# Update files in reviews directory
reviews_dir = os.path.join(base_dir, 'reviews')
if os.path.exists(reviews_dir):
    for filename in os.listdir(reviews_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(reviews_dir, filename)
            if update_file(filepath):
                updated_files.append(filepath)

# Update files in guides directory
guides_dir = os.path.join(base_dir, 'guides')
if os.path.exists(guides_dir):
    for filename in os.listdir(guides_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(guides_dir, filename)
            if update_file(filepath):
                updated_files.append(filepath)

# Update files in blog directory if it exists
blog_dir = os.path.join(base_dir, 'blog')
if os.path.exists(blog_dir):
    for filename in os.listdir(blog_dir):
        if filename.endswith('.html'):
            filepath = os.path.join(blog_dir, filename)
            if update_file(filepath):
                updated_files.append(filepath)

# Update root level files (excluding index.html which was already updated)
for filename in os.listdir(base_dir):
    if filename.endswith('.html') and filename != 'index.html':
        filepath = os.path.join(base_dir, filename)
        if os.path.isfile(filepath):
            # For root level files, check if they use reviews/ prefix
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                if 'reviews/sports-research-astaxanthin-review.html' in content:
                    # Has reviews/ prefix
                    original = content
                    content = content.replace(
                        '''<a href="/reviews" role="menuitem" class="dropdown-toggle">Reviews <i class="fas fa-chevron-down"></i></a>
                    <ul class="dropdown-menu" role="menu">
                        <li role="none"><a href="reviews/sports-research-astaxanthin-review.html" role="menuitem">#1: Sports Research</a></li>
                        <li role="none"><a href="reviews/life-extension-astaxanthin-review.html" role="menuitem">#2: Life Extension</a></li>
                        <li role="none"><a href="reviews/nutrex-hawaii-bioastin-review.html" role="menuitem">#3: NUTREX HAWAII BioAstin</a></li>
                    </ul>''',
                        new_menu_other
                    )
                    if content != original:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(content)
                        updated_files.append(filepath)
            except Exception as e:
                print(f"Error checking {filepath}: {e}")

print(f"Updated {len(updated_files)} files:")
for filepath in updated_files:
    print(f"  - {os.path.basename(filepath)}")

# Best Astaxanthin Website - Design System

## Overview
This design system ensures visual consistency, optimal user experience, and high conversion rates across the entire Best Astaxanthin affiliate website.

---

## 1. Brand Identity

### Brand Personality
- **Trustworthy**: Scientific, evidence-based, transparent
- **Professional**: Clean, organized, authoritative
- **Helpful**: Clear, accessible, user-focused
- **Modern**: Fresh, contemporary, optimized

### Brand Voice
- **Tone**: Informative yet conversational
- **Style**: Clear and concise, avoiding jargon
- **Approach**: Helpful expert, not pushy salesperson

---

## 2. Color Palette

### Primary Colors
```
Primary Red (Astaxanthin Color)
- Main: #FF6B6B (Coral Red - represents astaxanthin pigment)
- Dark: #E85555
- Light: #FF8787
- Usage: CTAs, highlights, product ratings, accents
```

```
Primary Blue (Trust & Health)
- Main: #4A90E2 (Sky Blue)
- Dark: #357ABD
- Light: #6BA3E8
- Usage: Links, secondary buttons, info boxes
```

### Secondary Colors
```
Complementary Green (Health & Wellness)
- Main: #51CF66 (Fresh Green)
- Dark: #40C057
- Light: #69DB7C
- Usage: Positive indicators, "Best Pick" badges, pros
```

```
Warm Orange (Energy & Vitality)
- Main: #FF922B (Vibrant Orange)
- Dark: #F76707
- Light: #FFA94D
- Usage: Sale tags, urgency indicators, highlights
```

### Neutral Colors
```
Text Colors
- Primary Text: #2C3E50 (Dark Slate)
- Secondary Text: #5A6C7D (Medium Gray)
- Muted Text: #95A5A6 (Light Gray)

Background Colors
- White: #FFFFFF
- Off-White: #F8F9FA
- Light Gray: #E9ECEF
- Medium Gray: #DEE2E6
```

### Alert Colors
```
Success: #51CF66 (Green)
Warning: #FFB84D (Orange)
Error: #FF6B6B (Red)
Info: #4A90E2 (Blue)
```

### Usage Guidelines
- **Primary CTA Buttons**: Primary Red (#FF6B6B)
- **Secondary Buttons**: Primary Blue (#4A90E2)
- **Links**: Primary Blue (#4A90E2)
- **Pros**: Complementary Green (#51CF66)
- **Cons**: Muted with error red icon
- **Sale/Discount Badges**: Warm Orange (#FF922B)
- **"Best Pick" Badge**: Complementary Green (#51CF66)

---

## 3. Typography

### Font Families

**Headings**:
```
Font: 'Poppins' (Google Fonts)
Fallback: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
Weights: 600 (SemiBold), 700 (Bold)
```

**Body Text**:
```
Font: 'Inter' (Google Fonts)
Fallback: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif
Weights: 400 (Regular), 500 (Medium), 600 (SemiBold)
```

**Accent/Numbers**:
```
Font: 'Poppins'
Usage: Ratings, prices, statistics
```

### Type Scale

**Desktop**:
```
H1 (Page Title): 48px / 700 / 1.2 line-height
H2 (Section Heading): 36px / 700 / 1.3 line-height
H3 (Product Name): 28px / 600 / 1.4 line-height
H4 (Subsection): 22px / 600 / 1.4 line-height
H5 (Minor Heading): 18px / 600 / 1.5 line-height
H6 (Small Heading): 16px / 600 / 1.5 line-height

Body Large: 18px / 400 / 1.7 line-height
Body Regular: 16px / 400 / 1.7 line-height
Body Small: 14px / 400 / 1.6 line-height
Caption: 12px / 400 / 1.5 line-height
```

**Mobile** (scaled down):
```
H1: 36px / 700 / 1.2 line-height
H2: 28px / 700 / 1.3 line-height
H3: 24px / 600 / 1.4 line-height
H4: 20px / 600 / 1.4 line-height
H5: 18px / 600 / 1.5 line-height
H6: 16px / 600 / 1.5 line-height

Body Regular: 16px / 400 / 1.7 line-height
Body Small: 14px / 400 / 1.6 line-height
```

### Typography Guidelines
- **Minimum font size**: 16px (for body text)
- **Maximum line length**: 70 characters for optimal readability
- **Paragraph spacing**: 1.5em between paragraphs
- **Letter spacing**: -0.02em for headings, normal for body

---

## 4. Spacing System

### Base Unit: 8px
All spacing follows an 8-point grid system for consistency.

```
Spacing Scale:
- xs: 4px (0.5 units)
- sm: 8px (1 unit)
- md: 16px (2 units)
- lg: 24px (3 units)
- xl: 32px (4 units)
- 2xl: 48px (6 units)
- 3xl: 64px (8 units)
- 4xl: 96px (12 units)
```

### Component Spacing

**Section Padding**:
- Desktop: 64px top/bottom, 32px left/right
- Mobile: 48px top/bottom, 16px left/right

**Card/Box Padding**:
- Desktop: 32px all sides
- Mobile: 24px all sides

**Element Margins**:
- Between major sections: 64px (desktop) / 48px (mobile)
- Between cards: 24px
- Between paragraphs: 16px
- Between list items: 12px

---

## 5. Layout & Grid

### Container Widths
```
Max Content Width: 1200px
Wide Content: 1400px
Narrow Content (articles): 800px
```

### Grid System
```
Desktop (12 columns):
- Column gap: 24px
- Margin: 32px

Tablet (8 columns):
- Column gap: 20px
- Margin: 24px

Mobile (4 columns):
- Column gap: 16px
- Margin: 16px
```

### Breakpoints
```
Mobile: 0-767px
Tablet: 768px-1023px
Desktop: 1024px-1439px
Large Desktop: 1440px+
```

### Common Layouts

**Two-Column Layout** (Desktop):
```
Main Content: 66.66% (8 columns)
Sidebar: 33.33% (4 columns)
Gap: 32px
```

**Three-Column Grid** (Product Cards):
```
Desktop: 3 columns
Tablet: 2 columns
Mobile: 1 column
Gap: 24px
```

---

## 6. Components

### 6.1 Buttons

**Primary Button (CTA)**:
```
Background: #FF6B6B (Primary Red)
Text: #FFFFFF (White)
Font: 16px / 600 (SemiBold)
Padding: 14px 32px
Border Radius: 8px
Box Shadow: 0 2px 8px rgba(255, 107, 107, 0.2)

Hover:
- Background: #E85555 (Darker)
- Box Shadow: 0 4px 12px rgba(255, 107, 107, 0.3)
- Transform: translateY(-2px)

Active:
- Transform: translateY(0)
```

**Secondary Button**:
```
Background: transparent
Border: 2px solid #4A90E2
Text: #4A90E2
Font: 16px / 600
Padding: 12px 32px
Border Radius: 8px

Hover:
- Background: #4A90E2
- Text: #FFFFFF
```

**Button Sizes**:
```
Large: 16px font, 16px 40px padding
Medium: 14px font, 12px 32px padding
Small: 12px font, 8px 24px padding
```

**Button States**:
- Default
- Hover (elevated, darker)
- Active (pressed)
- Disabled (50% opacity, no pointer)

### 6.2 Product Cards

**Card Structure**:
```
Container:
- Background: #FFFFFF
- Border: 1px solid #E9ECEF
- Border Radius: 12px
- Padding: 24px
- Box Shadow: 0 2px 8px rgba(0, 0, 0, 0.08)

Hover:
- Box Shadow: 0 8px 24px rgba(0, 0, 0, 0.12)
- Transform: translateY(-4px)
- Transition: all 0.3s ease

Layout:
1. Badge/Rank (top-left corner)
2. Product Image (centered, max 200px)
3. Product Name (H3)
4. Star Rating (with count)
5. Key Features (3-5 bullet points)
6. Price (large, bold)
7. CTA Button (full-width or centered)
```

**Badge Styles**:
```
"Best Overall" Badge:
- Background: #51CF66 (Green)
- Text: #FFFFFF
- Position: Absolute top-left
- Padding: 6px 12px
- Border Radius: 0 0 8px 0
- Font: 12px / 700

"Best Value" Badge:
- Background: #FF922B (Orange)

"Editor's Choice" Badge:
- Background: #4A90E2 (Blue)
```

### 6.3 Comparison Table

**Table Design**:
```
Container:
- Background: #FFFFFF
- Border: 1px solid #E9ECEF
- Border Radius: 12px
- Overflow: hidden
- Box Shadow: 0 4px 12px rgba(0, 0, 0, 0.08)

Header Row:
- Background: #F8F9FA
- Font: 14px / 600
- Text: #2C3E50
- Padding: 16px
- Border Bottom: 2px solid #DEE2E6

Data Rows:
- Padding: 16px
- Border Bottom: 1px solid #F1F3F5
- Alternating Background: #FFFFFF / #FAFBFC

Hover State:
- Background: #F8F9FA
```

**Table Columns**:
1. Rank/Badge (50px)
2. Product Image + Name (250px)
3. Rating (120px)
4. Key Features (200px)
5. Price (100px)
6. CTA Button (150px)

**Mobile Table**:
- Convert to stacked cards
- Each product = one card
- Horizontal scroll for wide tables

### 6.4 Rating Stars

**Star Display**:
```
Size: 20px (desktop) / 18px (mobile)
Filled Star: #FF922B (Orange)
Empty Star: #DEE2E6 (Light Gray)
Half Star: Gradient fill

Layout:
★★★★★ 4.7 (2,341 reviews)

Font: 14px / 600
Color: #5A6C7D
Spacing: 8px between stars and number
```

### 6.5 Pros & Cons Lists

**Pros List**:
```
Icon: ✓ (Checkmark)
Icon Color: #51CF66 (Green)
Icon Size: 20px
Text: 16px / 400
Line Height: 1.7
Spacing: 12px between items

Layout:
✓ High potency formula (12mg)
✓ Natural astaxanthin from algae
✓ Third-party tested for purity
```

**Cons List**:
```
Icon: ✗ (X mark)
Icon Color: #FF6B6B (Red)
Icon Size: 20px
Text: 16px / 400
Line Height: 1.7
Spacing: 12px between items
```

### 6.6 Info Boxes

**General Info Box**:
```
Background: #E8F4FD (Light Blue)
Border-Left: 4px solid #4A90E2
Padding: 20px 24px
Border Radius: 8px
Icon: ℹ️ (info icon)
```

**Success Box**:
```
Background: #E6FCF0 (Light Green)
Border-Left: 4px solid #51CF66
```

**Warning Box**:
```
Background: #FFF4E6 (Light Orange)
Border-Left: 4px solid #FF922B
```

**Tip Box**:
```
Background: #FEF3E6 (Light Yellow)
Border-Left: 4px solid #FFB84D
Icon: 💡 (lightbulb)
```

### 6.7 Price Display

**Regular Price**:
```
Font: 32px / 700 (Poppins)
Color: #2C3E50
Format: $29.99
```

**Sale Price**:
```
New Price: 32px / 700
Color: #FF6B6B (Red)
Old Price: 20px / 400, strikethrough
Color: #95A5A6
Format: $29.99 $39.99
Savings Badge: "Save 25%" in green
```

**Price per Serving**:
```
Font: 14px / 400
Color: #5A6C7D
Format: ($0.50 per serving)
Display below main price
```

### 6.8 Images

**Product Images**:
```
Aspect Ratio: 1:1 (square)
Size: 400x400px (displayed at 200x200px for retina)
Format: WebP with JPG fallback
Background: White or transparent
Border Radius: 8px
Shadow: 0 2px 8px rgba(0, 0, 0, 0.08)
```

**Featured Images (Hero)**:
```
Aspect Ratio: 16:9
Size: 1200x675px minimum
Format: WebP with JPG fallback
Overlay: Optional dark overlay (0.3 opacity)
```

**Thumbnails**:
```
Size: 100x100px
Border Radius: 6px
Border: 1px solid #E9ECEF
```

### 6.9 Navigation Header

**Desktop Header**:
```
Height: 80px
Background: #FFFFFF
Box Shadow: 0 2px 8px rgba(0, 0, 0, 0.08)
Position: Sticky top

Logo:
- Height: 40px
- Left aligned

Menu:
- Font: 16px / 500
- Color: #2C3E50
- Spacing: 32px between items
- Hover: Color changes to #FF6B6B

Search:
- Right aligned
- Icon button style
```

**Mobile Header**:
```
Height: 64px
Hamburger Menu: Right side
Logo: Centered or left
Sticky on scroll
```

### 6.10 Footer

**Footer Design**:
```
Background: #2C3E50 (Dark Slate)
Text Color: #FFFFFF
Padding: 48px 0

Sections (4 columns on desktop):
1. About/Logo
2. Quick Links
3. Resources
4. Contact/Social

Link Hover: #FF6B6B
Font: 14px / 400

Bottom Bar:
- Background: #1A252F (Darker)
- Copyright + Legal Links
- Padding: 24px 0
```

---

## 7. Interactive Elements

### Hover Effects
```
Cards:
- Transform: translateY(-4px)
- Shadow: Increase depth
- Transition: 0.3s ease

Buttons:
- Transform: translateY(-2px)
- Shadow: Increase
- Background: Darken 10%
- Transition: 0.2s ease

Links:
- Color: Lighten 10%
- Underline appears
- Transition: 0.2s ease
```

### Transitions
```
Default: all 0.3s ease
Fast: 0.15s ease
Slow: 0.5s ease

Easing Functions:
- Ease-out: For entering elements
- Ease-in: For exiting elements
- Ease-in-out: For state changes
```

### Animations
```
Fade In:
- Opacity: 0 to 1
- Duration: 0.5s
- Used for content loading

Slide Up:
- Transform: translateY(20px) to 0
- Opacity: 0 to 1
- Duration: 0.6s
- Used for scroll-triggered elements

Pulse (for CTAs):
- Scale: 1 to 1.05 to 1
- Duration: 2s infinite
- Subtle attention grabber
```

---

## 8. Icons

### Icon System
**Library**: Font Awesome 6 (Free) or Heroicons

**Common Icons**:
```
- Star (filled/empty): Ratings
- Check: Pros, features
- X: Cons
- Shopping Cart: Purchase
- External Link: Affiliate links
- Info Circle: Information
- Award: Best pick badge
- Truck: Shipping info
- Shield: Security/quality
- Search: Search function
```

**Icon Sizes**:
```
Small: 16px
Medium: 20px
Large: 24px
XL: 32px
```

**Icon Colors**:
- Match text color by default
- Use brand colors for emphasis
- Hover: Lighten or change to brand color

---

## 9. Forms

### Input Fields
```
Height: 48px
Padding: 12px 16px
Border: 2px solid #DEE2E6
Border Radius: 8px
Font: 16px / 400
Background: #FFFFFF

Focus State:
- Border: 2px solid #4A90E2
- Box Shadow: 0 0 0 3px rgba(74, 144, 226, 0.1)
- Outline: none

Error State:
- Border: 2px solid #FF6B6B
- Error message: 14px, #FF6B6B
```

### Search Bar
```
Width: 100% (mobile) / 400px (desktop)
Height: 48px
Border Radius: 24px (rounded pill)
Padding: 12px 20px 12px 48px
Icon: Left-aligned, 20px
Border: 2px solid #E9ECEF

Focus:
- Border: 2px solid #4A90E2
- Shadow: 0 0 0 3px rgba(74, 144, 226, 0.1)
```

### Email Signup Form
```
Layout: Horizontal (desktop) / Stacked (mobile)
Input + Button combined
Input takes 70%, Button 30%
Height: 56px
Border Radius: 8px
```

---

## 10. Badges & Labels

### Product Badges
```
"Best Overall":
- Background: Linear gradient #51CF66 to #40C057
- Text: #FFFFFF
- Font: 12px / 700
- Padding: 6px 12px
- Border Radius: 20px (pill)

"New":
- Background: #4A90E2
- Pulse animation

"Sale":
- Background: #FF6B6B
- Text: "20% OFF"

"Out of Stock":
- Background: #95A5A6
- Opacity: 0.7
```

### Info Labels
```
Shipping:
- Icon: Truck
- Text: "Free Shipping"
- Color: #51CF66

Money-Back:
- Icon: Shield
- Text: "60-Day Guarantee"
- Color: #4A90E2

Third-Party Tested:
- Icon: Award
- Text: "Lab Tested"
- Color: #FF922B
```

---

## 11. Responsive Design

### Mobile-First Approach
Design for mobile, then enhance for larger screens.

### Key Breakpoints
```
Mobile: 320px - 767px
Tablet: 768px - 1023px
Desktop: 1024px - 1439px
Large: 1440px+
```

### Mobile Optimizations
```
- Stack columns vertically
- Full-width buttons
- Larger tap targets (min 48x48px)
- Simplified navigation (hamburger)
- Reduced spacing
- Larger fonts (min 16px to prevent zoom)
- Sticky CTA buttons
- Collapsible sections for long content
```

### Tablet Optimizations
```
- 2-column layouts
- Larger images
- Show more content
- Reduced hamburger use
```

---

## 12. Accessibility

### Color Contrast
```
Text on White: Minimum 4.5:1 ratio
Large Text (18px+): Minimum 3:1 ratio
All colors chosen meet WCAG AA standards
```

### Focus States
```
All interactive elements have visible focus
Focus outline: 3px solid #4A90E2
Offset: 2px
Never remove :focus without alternative
```

### Alt Text
```
All images require descriptive alt text
Decorative images: alt=""
Product images: "Product Name - Astaxanthin Supplement Bottle"
```

### Semantic HTML
```
Use proper heading hierarchy (H1 → H2 → H3)
<nav> for navigation
<main> for main content
<article> for blog posts
<aside> for sidebars
<button> for buttons (not <div>)
```

### Keyboard Navigation
```
Tab order follows logical flow
Skip to content link
All interactive elements accessible via keyboard
No keyboard traps
```

### Screen Reader Support
```
ARIA labels where needed
Image alt text
Form labels properly associated
Error messages announced
```

---

## 13. Performance

### Image Optimization
```
Format: WebP with JPG/PNG fallback
Compression: 80% quality
Lazy loading: Below the fold
Responsive images: srcset for different sizes
Max file size: 200KB per image
```

### Code Optimization
```
Minify CSS/JS
Combine files where possible
Defer non-critical JavaScript
Critical CSS inline
Remove unused CSS
```

### Loading Performance
```
Target Metrics:
- First Contentful Paint: <1.8s
- Largest Contentful Paint: <2.5s
- Time to Interactive: <3.8s
- Cumulative Layout Shift: <0.1
```

---

## 14. Content Formatting

### Paragraph Style
```
Max width: 700px
Line height: 1.7
Margin bottom: 16px
Justified: Left (never full justify)
Font size: 16px minimum
```

### Lists
```
Bullet Points:
- Custom bullet: colored circle or checkmark
- Indent: 24px
- Spacing: 12px between items
- Line height: 1.6

Numbered Lists:
- Bold numbers in brand color
- Same spacing as bullets
```

### Blockquotes
```
Border-left: 4px solid #FF6B6B
Padding: 20px 24px
Background: #F8F9FA
Font-style: italic
Font-size: 18px
Color: #5A6C7D
```

### Tables
```
Border: 1px solid #E9ECEF
Cell padding: 16px
Header background: #F8F9FA
Alternating rows: #FFFFFF / #FAFBFC
Mobile: Responsive/stacked
```

---

## 15. Photography & Imagery Guidelines

### Product Photography
```
Style: Clean, professional
Background: White or very light gray
Lighting: Bright, even, no harsh shadows
Angle: Slight 3/4 angle showing label
Context: Occasionally show with props (glass of water, etc.)
```

### Hero Images
```
Style: High-quality, vibrant
Subject: Health, wellness, active lifestyle
Overlay: Optional dark overlay for text readability
Text contrast: Ensure minimum 4.5:1 ratio
```

### Infographics
```
Brand colors only
Clean, minimal design
Sans-serif fonts
White or light background
Export as SVG when possible
```

---

## 16. Animation Guidelines

### When to Animate
```
✓ Page transitions
✓ Hover states
✓ Loading indicators
✓ Scroll-triggered reveals
✓ Success confirmations

✗ Avoid excessive motion
✗ No auto-playing videos (accessibility)
✗ Respect prefers-reduced-motion
```

### Animation Duration
```
Micro-interactions: 150-200ms
UI transitions: 200-300ms
Page transitions: 300-500ms
Loading animations: Infinite (with fallback)
```

---

## 17. Design Patterns

### Comparison Pattern
```
Side-by-side product comparison
Sticky header row
Highlight differences
"Winner" indicator for categories
Mobile: Swipeable cards
```

### Progressive Disclosure
```
"Read More" buttons for long content
Expandable FAQ items
Tabbed content areas
Collapsible sections on mobile
```

### Social Proof
```
Star ratings prominent
Review count visible
Testimonials with photos
"X people bought this" indicators
Trust badges (certified, tested, etc.)
```

---

## 18. Conversion Optimization Elements

### Urgency Indicators
```
"Limited Time Offer"
Countdown timers (when applicable)
Stock level indicators
"Sale Ends Soon" badges
Color: Orange (#FF922B)
Position: Near price/CTA
```

### Trust Builders
```
Money-back guarantee badges
Secure checkout indicators
"As Seen On" logos
Certifications (GMP, Third-party tested)
Author credentials
Methodology transparency
```

### CTA Hierarchy
```
Primary CTA:
- Large, prominent
- Brand color (#FF6B6B)
- Above the fold
- Action-oriented text

Secondary CTA:
- Smaller
- Outline style
- "Learn More" or "Compare"

Tertiary:
- Text link style
- Subtle
```

---

## 19. Dark Mode (Optional Future Enhancement)

### Dark Palette
```
Background: #1A1A1A
Surface: #2C2C2C
Text Primary: #FFFFFF
Text Secondary: #B0B0B0

Adapt brand colors:
- Primary Red: #FF8787 (lighter)
- Primary Blue: #6BA3E8 (lighter)
- Reduce shadows, use borders
```

---

## 20. Design Checklist

### Before Launch
```
□ All colors meet WCAG AA contrast ratios
□ All images have alt text
□ Focus states visible on all interactive elements
□ Mobile responsive at all breakpoints
□ Buttons minimum 48x48px tap target
□ Forms have proper labels and error states
□ Typography scale is consistent
□ Spacing follows 8px grid
□ Images optimized (WebP, compressed)
□ Loading states for all async actions
□ Hover states on all interactive elements
□ Print stylesheet (optional)
□ Favicon and touch icons
□ Open Graph images for social sharing
```

---

## 21. File Organization

### Design Assets
```
/assets
  /images
    /products
    /logos
    /icons
    /hero
  /fonts
    /poppins
    /inter
  /styles
    /components
    /utilities
    /base
```

### Naming Conventions
```
Images: lowercase-with-hyphens
- product-astaxanthin-brand-name.webp
- icon-checkmark-green.svg
- hero-healthy-lifestyle.jpg

CSS Classes: BEM methodology
- block__element--modifier
- product-card__title
- btn--primary
```

---

## 22. Tools & Resources

### Design Tools
- Figma (design mockups)
- Adobe Photoshop/Illustrator (image editing)
- Canva (quick graphics)
- Coolors.co (color palette generator)

### Development Tools
- Chrome DevTools (responsive testing)
- WAVE (accessibility checker)
- Google Lighthouse (performance)
- WebPageTest (speed testing)

### Font Resources
- Google Fonts (Poppins, Inter)
- Font Awesome (icons)

### Stock Photos
- Unsplash
- Pexels
- Pixabay

---

## Conclusion

This design system ensures:
- **Consistency** across all pages
- **High conversion rates** through proven UX patterns
- **Accessibility** for all users
- **Professional appearance** that builds trust
- **Fast performance** for better SEO
- **Scalability** as the site grows

Refer to this document for all design decisions to maintain brand consistency and optimal user experience.

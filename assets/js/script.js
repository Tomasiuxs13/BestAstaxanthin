/**
 * Best Astaxanthin - Main JavaScript
 * Handles interactive elements and user interactions
 */

(function() {
    'use strict';

    // ===================================
    // 1. Mobile Menu Toggle
    // ===================================

    const menuToggle = document.querySelector('.menu-toggle');
    const navMenu = document.querySelector('.nav-menu');

    if (menuToggle && navMenu) {
        menuToggle.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('active');
        });

        // Close menu when clicking on a link
        const navLinks = navMenu.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!menuToggle.contains(event.target) && !navMenu.contains(event.target)) {
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // ===================================
    // 2. FAQ Accordion
    // ===================================

    const faqToggles = document.querySelectorAll('.faq-toggle');

    faqToggles.forEach(toggle => {
        toggle.addEventListener('click', function() {
            const faqItem = this.closest('.faq-item');
            const faqAnswer = faqItem.querySelector('.faq-answer');
            const isExpanded = this.getAttribute('aria-expanded') === 'true';

            // Close all other FAQ items
            faqToggles.forEach(otherToggle => {
                if (otherToggle !== toggle) {
                    otherToggle.setAttribute('aria-expanded', 'false');
                    otherToggle.closest('.faq-item').classList.remove('active');
                }
            });

            // Toggle current item
            this.setAttribute('aria-expanded', !isExpanded);
            faqItem.classList.toggle('active');

            // Set max-height for smooth animation
            if (!isExpanded) {
                faqAnswer.style.maxHeight = faqAnswer.scrollHeight + 'px';
            } else {
                faqAnswer.style.maxHeight = '0';
            }
        });
    });

    // ===================================
    // 3. Smooth Scroll for Anchor Links
    // ===================================

    const anchorLinks = document.querySelectorAll('a[href^="#"]');

    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Skip if it's just "#"
            if (href === '#') {
                e.preventDefault();
                return;
            }

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();

                // Get header height for offset
                const header = document.querySelector('.header');
                const headerHeight = header ? header.offsetHeight : 0;

                const targetPosition = target.offsetTop - headerHeight - 20;

                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });

                // Update URL without jumping
                history.pushState(null, null, href);
            }
        });
    });

    // ===================================
    // 4. Sticky Mobile CTA Show/Hide
    // ===================================

    const stickyCTA = document.querySelector('.sticky-mobile-cta');
    const heroSection = document.querySelector('.hero');

    if (stickyCTA && heroSection) {
        window.addEventListener('scroll', function() {
            const heroBottom = heroSection.offsetTop + heroSection.offsetHeight;
            const scrollPosition = window.pageYOffset || document.documentElement.scrollTop;

            if (scrollPosition > heroBottom) {
                stickyCTA.style.transform = 'translateY(0)';
                stickyCTA.style.opacity = '1';
            } else {
                stickyCTA.style.transform = 'translateY(100%)';
                stickyCTA.style.opacity = '0';
            }
        });

        // Initialize with hidden state
        stickyCTA.style.transition = 'all 0.3s ease';
        stickyCTA.style.transform = 'translateY(100%)';
        stickyCTA.style.opacity = '0';
    }

    // ===================================
    // 5. Scroll Animations
    // ===================================

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Animate product cards on scroll
    const productCards = document.querySelectorAll('.product-card');
    productCards.forEach((card, index) => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = `opacity 0.6s ease ${index * 0.1}s, transform 0.6s ease ${index * 0.1}s`;
        observer.observe(card);
    });

    // ===================================
    // 6. Track Affiliate Link Clicks (Analytics)
    // ===================================

    const affiliateLinks = document.querySelectorAll('a[rel*="nofollow"]');

    affiliateLinks.forEach(link => {
        link.addEventListener('click', function() {
            const productName = this.closest('.product-card')?.querySelector('h3')?.textContent || 'Unknown Product';
            const position = this.closest('.product-card')?.querySelector('.rank-number')?.textContent || 'Unknown';

            // Track with Google Analytics (if implemented)
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    'event_category': 'Affiliate Link',
                    'event_label': productName,
                    'value': position
                });
            }

            // Track with any other analytics platform
            console.log('Affiliate link clicked:', {
                product: productName,
                position: position,
                url: this.href
            });
        });
    });

    // ===================================
    // 7. Table Sorting (Optional Enhancement)
    // ===================================

    function sortTable(table, column, asc = true) {
        const tbody = table.querySelector('tbody');
        const rows = Array.from(tbody.querySelectorAll('tr'));

        rows.sort((a, b) => {
            const aValue = a.querySelectorAll('td')[column].textContent.trim();
            const bValue = b.querySelectorAll('td')[column].textContent.trim();

            // Try to parse as number
            const aNum = parseFloat(aValue.replace(/[^0-9.]/g, ''));
            const bNum = parseFloat(bValue.replace(/[^0-9.]/g, ''));

            if (!isNaN(aNum) && !isNaN(bNum)) {
                return asc ? aNum - bNum : bNum - aNum;
            }

            return asc ? aValue.localeCompare(bValue) : bValue.localeCompare(aValue);
        });

        // Re-append rows in new order
        rows.forEach(row => tbody.appendChild(row));
    }

    // Add sorting to table headers (if needed in future)
    const tableHeaders = document.querySelectorAll('.comparison-table th');
    tableHeaders.forEach((header, index) => {
        header.style.cursor = 'pointer';
        header.addEventListener('click', function() {
            const table = this.closest('table');
            const isAsc = this.classList.contains('sort-asc');

            // Remove sort classes from all headers
            tableHeaders.forEach(h => h.classList.remove('sort-asc', 'sort-desc'));

            // Add sort class to clicked header
            this.classList.add(isAsc ? 'sort-desc' : 'sort-asc');

            sortTable(table, index, !isAsc);
        });
    });

    // ===================================
    // 8. Back to Top Button (Optional)
    // ===================================

    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTop.className = 'back-to-top';
    backToTop.setAttribute('aria-label', 'Back to top');
    backToTop.style.cssText = `
        position: fixed;
        bottom: 80px;
        right: 20px;
        width: 50px;
        height: 50px;
        background-color: var(--color-primary-red, #FF6B6B);
        color: white;
        border: none;
        border-radius: 50%;
        font-size: 20px;
        cursor: pointer;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
        z-index: 80;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
    `;

    document.body.appendChild(backToTop);

    window.addEventListener('scroll', function() {
        if (window.pageYOffset > 500) {
            backToTop.style.opacity = '1';
            backToTop.style.visibility = 'visible';
        } else {
            backToTop.style.opacity = '0';
            backToTop.style.visibility = 'hidden';
        }
    });

    backToTop.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });

    backToTop.addEventListener('mouseenter', function() {
        this.style.transform = 'translateY(-5px)';
        this.style.boxShadow = '0 6px 16px rgba(0, 0, 0, 0.3)';
    });

    backToTop.addEventListener('mouseleave', function() {
        this.style.transform = 'translateY(0)';
        this.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.2)';
    });

    // ===================================
    // 9. Lazy Loading Images (Performance)
    // ===================================

    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }
                    imageObserver.unobserve(img);
                }
            });
        });

        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // ===================================
    // 10. Copy Link Functionality
    // ===================================

    function copyToClipboard(text) {
        if (navigator.clipboard && navigator.clipboard.writeText) {
            navigator.clipboard.writeText(text).then(() => {
                showNotification('Link copied to clipboard!');
            }).catch(() => {
                fallbackCopyTextToClipboard(text);
            });
        } else {
            fallbackCopyTextToClipboard(text);
        }
    }

    function fallbackCopyTextToClipboard(text) {
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            document.execCommand('copy');
            showNotification('Link copied to clipboard!');
        } catch (err) {
            console.error('Failed to copy text: ', err);
        }

        document.body.removeChild(textArea);
    }

    function showNotification(message) {
        const notification = document.createElement('div');
        notification.textContent = message;
        notification.style.cssText = `
            position: fixed;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            background-color: #2C3E50;
            color: white;
            padding: 12px 24px;
            border-radius: 8px;
            z-index: 1000;
            animation: slideUp 0.3s ease;
        `;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.opacity = '0';
            notification.style.transition = 'opacity 0.3s ease';
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }

    // ===================================
    // 11. Keyboard Navigation Enhancement
    // ===================================

    // Trap focus in mobile menu when open
    if (menuToggle && navMenu) {
        menuToggle.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                this.click();
            }
        });
    }

    // Handle escape key to close mobile menu
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            if (navMenu && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
                menuToggle.focus();
            }

            // Close any open FAQ items
            faqToggles.forEach(toggle => {
                if (toggle.getAttribute('aria-expanded') === 'true') {
                    toggle.click();
                }
            });
        }
    });

    // ===================================
    // 12. Performance Monitoring
    // ===================================

    if ('PerformanceObserver' in window) {
        // Largest Contentful Paint (LCP)
        const lcpObserver = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            const lastEntry = entries[entries.length - 1];
            console.log('LCP:', lastEntry.renderTime || lastEntry.loadTime);
        });
        lcpObserver.observe({ entryTypes: ['largest-contentful-paint'] });

        // First Input Delay (FID)
        const fidObserver = new PerformanceObserver((list) => {
            const entries = list.getEntries();
            entries.forEach(entry => {
                console.log('FID:', entry.processingStart - entry.startTime);
            });
        });
        fidObserver.observe({ entryTypes: ['first-input'] });

        // Cumulative Layout Shift (CLS)
        let clsScore = 0;
        const clsObserver = new PerformanceObserver((list) => {
            for (const entry of list.getEntries()) {
                if (!entry.hadRecentInput) {
                    clsScore += entry.value;
                }
            }
            console.log('CLS:', clsScore);
        });
        clsObserver.observe({ entryTypes: ['layout-shift'] });
    }

    // ===================================
    // 13. Page Load Complete
    // ===================================

    window.addEventListener('load', function() {
        console.log('Best Astaxanthin - Page fully loaded');

        // Remove any loading states
        document.body.classList.add('loaded');

        // Log performance metrics
        if (window.performance && window.performance.timing) {
            const perfData = window.performance.timing;
            const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
            console.log('Page load time:', pageLoadTime + 'ms');
        }
    });

    // ===================================
    // 14. Initialize Everything
    // ===================================

    console.log('Best Astaxanthin - Scripts initialized');

})();

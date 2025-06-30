"""
SEO Configuration Manager
Centralized settings for SEO management across the application.
"""

from typing import Dict, List, Optional
from django.conf import settings


class SEOConfig:
    """Centralized SEO configuration and constants."""
    
    # Default values
    DEFAULT_TITLE_SUFFIX = "hardikbaraiya.com"
    DEFAULT_SEPARATOR = " | "
    DEFAULT_DESCRIPTION_LENGTH = 160
    DEFAULT_KEYWORDS_COUNT = 15
    
    # Social media defaults
    DEFAULT_OG_TYPE = "website"
    DEFAULT_TWITTER_CARD = "summary_large_image"
    DEFAULT_TWITTER_SITE = "@hardix02"
    
    # Site information
    SITE_NAME = "hardikbaraiya.com"
    AUTHOR = "HardikBaraiya"
    SITE_URL = getattr(settings, 'SITE_URL', 'https://hardikbaraiya.com')
    DEFAULT_IMAGE = f"{SITE_URL}/static/img/default-og-image.webp"
    
    # Content type specific settings
    CONTENT_TYPES = {
        'homepage': {
            'og_type': 'website',
            'twitter_card': 'summary_large_image',
            'priority': 1.0,
            'changefreq': 'weekly'
        },
        'blog_list': {
            'og_type': 'website', 
            'twitter_card': 'summary_large_image',
            'priority': 0.9,
            'changefreq': 'daily'
        },
        'blog_detail': {
            'og_type': 'article',
            'twitter_card': 'summary_large_image', 
            'priority': 0.8,
            'changefreq': 'monthly'
        },
        'project_list': {
            'og_type': 'website',
            'twitter_card': 'summary_large_image',
            'priority': 0.9,
            'changefreq': 'monthly'
        },
        'project_detail': {
            'og_type': 'website',
            'twitter_card': 'summary_large_image',
            'priority': 0.8,
            'changefreq': 'monthly'
        },
        'dashboard': {
            'og_type': 'website',
            'twitter_card': 'summary_large_image',
            'priority': 0.7,
            'changefreq': 'daily'
        },
        'about': {
            'og_type': 'profile',
            'twitter_card': 'summary_large_image',
            'priority': 1.0,
            'changefreq': 'monthly'
        },
        'contact': {
            'og_type': 'website',
            'twitter_card': 'summary',
            'priority': 0.8,
            'changefreq': 'monthly'
        },
        'guestbook': {
            'og_type': 'website',
            'twitter_card': 'summary_large_image',
            'priority': 0.7,
            'changefreq': 'daily'
        },
        'privacy_policy': {
            'og_type': 'website',
            'twitter_card': 'summary',
            'priority': 0.5,
            'changefreq': 'yearly'
        }
    }
    
    # Common keywords by category
    COMMON_KEYWORDS = {
        'personal': [
            'hardix', 'Hardik Baraiya', 'hardikbaraiya.com',
            'hardix blog', 'hardix portfolio',
            'software developer', 'web developer', 'python developer',
            'MQL EA Exper', 'WordPress developer', 'full stack developer'
        ],
        'technical': [
            'C#', 'Python', 'JavaScript',
            'C++', 'React', 'MQL', 'Web Development'
        ],
        'content': [
            'portfolio', 'blog', 'tutorials', 'coding', 'programming',
            'tech insights', 'development tips', 'project showcase'
        ],
        'location': [
            'India', 'Indian developer', 'South Asia',
            'Gujarat developer', 'Indian tech', 'South Asian tech'
        ]
    }
    
    # Schema.org templates
    SCHEMA_TEMPLATES = {
        'person': {
            "@context": "https://schema.org",
            "@type": "Person",
            "name": AUTHOR,
            "url": SITE_URL,
            "sameAs": [],  # Will be populated dynamically
            "jobTitle": "Software Developer & Web Developer",
            "worksFor": {
                "@type": "Organization",
                "name": "Freelance"
            }
        },
        'website': {
            "@context": "https://schema.org", 
            "@type": "WebSite",
            "name": SITE_NAME,
            "url": SITE_URL,
            "author": {
                "@type": "Person",
                "name": AUTHOR
            }
        },
        'blog': {
            "@context": "https://schema.org",
            "@type": "Blog",
            "name": f"{AUTHOR}'s Blog",
            "url": f"{SITE_URL}/blog/",
            "author": {
                "@type": "Person",
                "name": AUTHOR
            }
        }
    }

project = 'verizon login'
author = 'verizon-login'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Bing search verification
html_context = {
    'bing_verification_code': 'B39742FA329BD6166A2DD3035563B540'
}

# Base URL for sitemap
html_baseurl = 'https://verizon-login.readthedocs.io/en/latest/'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',  # Add this line
]
# Add at the bottom
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
SECRET_KEY = '{{ secret_key }}'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = []

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)
CASHCOG_EXPENSE_API_URL = os.environ.get('CASHCOG_EXPENSE_API_URL', '')

try:
    from .local import *
except:
    pass

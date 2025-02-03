# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
from api.settings import env

DATABASES = {'default': env.db()}
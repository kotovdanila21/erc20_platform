# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
import os

from api.settings import BASE_DIR

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")
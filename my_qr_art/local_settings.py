from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n_!=%bx3=^o0t4df^cmd5%$5d-8d%_vgmdcwq-ia7be4g=1zf0'

DEBUG = True

ALLOWED_HOSTS = ['*']

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'

STATICFILES_DIRS = [
        BASE_DIR / "static",
]

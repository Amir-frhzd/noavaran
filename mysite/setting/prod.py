from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w69mo_ei@&y@8!6_%t_jy0#jo01po!3#fphq&m0yb&j8sa^r)r'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['setaresiah.com','www.setaresiah.com']

# sites framework
SITE_ID = 2
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'setaresi_setaresiah',
        'USER': 'setaresi_amir',
        'PASSWORD': '3g@uSDfMY_hz',
        'HOST':'localhost',
        'PORT':'3306',
    }
}
STATIC_ROOT=BASE_DIR/'static'
MEDIA_ROOT=BASE_DIR/'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]
X_FRAME_OPTIONS = "SAMEORIGIN"

SECURE_BROWSER_XSS_FILTER = True
#X-Content-Type-Options
SECURE_CONTENT_TYPE_NOSNIFF = True

## Strict-Transport-Security
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
SECURE_SSL_REDIRECT = True 

# for more security
CSRF_COOKIE_SECURE = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Strict'

# Keep our policy as strict as possible
CSP_DEFAULT_SRC = ("'none'",)
CSP_STYLE_SRC = ("'self'", 'fonts.googleapis.com')
CSP_SCRIPT_SRC = ("'self'",)
CSP_FONT_SRC = ("'self'", 'fonts.gstatic.com')
CSP_IMG_SRC = ("'self'",)
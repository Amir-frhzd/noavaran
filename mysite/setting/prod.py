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
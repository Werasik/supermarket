from pathlib import Path
import os

# Базовий каталог проекту
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретний ключ для Django
SECRET_KEY = 'django-insecure-(oyvqmt4l!o@lwo=%opnk7ca-)fhyr+@00v%_!knze-vvim-ja'

# Режим відладки
DEBUG = True

# Дозволені хости
ALLOWED_HOSTS = []

# Додатки
INSTALLED_APPS = [
    'Products',
    'cart',
    'orders',
    'users',
    'payments',
    'shipping',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Головний конфігураційний файл URL
ROOT_URLCONF = 'supermarket.urls'

# Налаштування шаблонів
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'supermarket.wsgi.application'

# База даних
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Валідатори паролів
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Налаштування мови та часової зони
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Статичні файли
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Медіа-файли
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Поле для автоматичного первинного ключа
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Налаштування PayPal
PAYPAL_CLIENT_ID = "ASRtmfnHrQS8Vba4lHWznXxIIE9S3AmC3Y4MyxcdsWjfHNZfrmF11C6TmD6oDfuHoAGBklT3z1ho-XYl"
PAYPAL_CLIENT_SECRET = "ELSveWgcGFt7yKKTKWcIoqkzZXDfssKjwVlq3RKGkg8RtejVf2tuqzHJGNUEbmBwIzSPZwCGJQzS7PuK"
PAYPAL_MODE = "sandbox"

# Налаштування Email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Наприклад, для Gmail
EMAIL_PORT = 587  # Порт для TLS
EMAIL_USE_TLS = True  # Увімкнення TLS
EMAIL_HOST_USER = 'klumenko2007maks@gmail.com'  # Ваша електронна пошта
EMAIL_HOST_PASSWORD = '137955137955max'
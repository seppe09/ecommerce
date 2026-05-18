<<<<<<< HEAD
import os
from pathlib import Path
from dotenv import load_dotenv
=======
from pathlib import Path
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

<<<<<<< HEAD
load_dotenv(BASE_DIR / ".env")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")
=======

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-wua&px4)ttd1chm#v7%p#_-u27q1ew60t$3$wwm7xig=r#&hk2"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
<<<<<<< HEAD
=======
    # Custom
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
    "apps.accounts",
    "apps.products",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
<<<<<<< HEAD
    "django.middleware.clickjacking.XFrameOptionsMiddleware", 
=======
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
]

ROOT_URLCONF = "ecommerce.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [ BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
<<<<<<< HEAD
                "django.template.context_processors.debug",
=======
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ecommerce.wsgi.application"


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}

AUTH_USER_MODEL = "accounts.User"

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
=======
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "ecommerce",
        "USER": "seppe",
        "PASSWORD": "123456",
        "HOST": "127.0.0.1",
        "PORT": 3306,
    }
}

# Password validation

AUTH_USER_MODEL = "accounts.User"
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
<<<<<<< HEAD
# https://docs.djangoproject.com/en/4.2/topics/i18n/
=======
>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


<<<<<<< HEAD
=======
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037
STATIC_URL = "static/"
STATICFILES_DIRS = [
        BASE_DIR / "static"
]

# Media files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

<<<<<<< HEAD
# Default primary key field type - ADD THIS LINE
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'secondary',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}
=======
    

>>>>>>> 9343361705b3308eacf22282d0e1047c41f89037

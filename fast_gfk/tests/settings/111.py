import os
import glob


BASE_DIR = os.path.join(
    glob.glob(os.environ["VIRTUAL_ENV"] +  "/lib/*/site-packages")[0],
    "fast_gfk"
)

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    }
}

INSTALLED_APPS = (
    "fast_gfk.tests",
    "django.contrib.contenttypes",
    "test_without_migrations",
)

SECRET_KEY = "SECRET_KEY"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
        ],
        "OPTIONS": {
        },
    },
]

import os

SITE_ID = 1
DEBUG = True

MEDIA_ROOT = os.path.normcase(os.path.dirname(os.path.abspath(__file__)))
MEDIA_URL = '/media/'

DATABASE_ENGINE = 'sqlite3'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.sessions',
    'django.contrib.auth',
    'django.contrib.admin',
    'rest_framework_3',
    'example.api',
]

ROOT_URLCONF = 'example.api.urls'

SECRET_KEY = 'abc123'

PASSWORD_HASHERS = ('django.contrib.auth.hashers.UnsaltedMD5PasswordHasher', )

MIDDLEWARE_CLASSES = ()

rest_framework_3 = {
    'PAGINATE_BY': 1,
    'PAGINATE_BY_PARAM': 'page_size',
    'MAX_PAGINATE_BY': 100,
    # DRF v3.1+
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework_ember_3.pagination.PageNumberPagination',
    # DRF v3.0 and older
    'DEFAULT_PAGINATION_SERIALIZER_CLASS':
        'rest_framework_ember_3.pagination.PaginationSerializer',
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework_ember_3.parsers.JSONParser',
        'rest_framework_3.parsers.FormParser',
        'rest_framework_3.parsers.MultiPartParser'
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework_ember_3.renderers.JSONRenderer',
        'rest_framework_3.renderers.JSONRenderer',
        'rest_framework_3.renderers.BrowsableAPIRenderer',
    ),
}

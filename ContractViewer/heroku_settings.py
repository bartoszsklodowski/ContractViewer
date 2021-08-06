from .settings import *
import dj_database_url
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgresql',
        }
    }

DATABASES['default'] =  dj_database_url.config(conn_max_age=600, ssl_require=True)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

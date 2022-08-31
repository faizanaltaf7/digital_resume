import django_on_heroku
from distutils.log import debug

from decouple import config

from resume_demo.settings.dev import ALLOWED_HOSTS, SECRET_KEY

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'https://faizanaltaf.herokuapp.com/',
    'https://git.heroku.com/faizanaltaf.git',
]

DEBUG_PROPAGATE_EXECEPTIONS = True
 
 LOGGING = {
    'version': 1,
    'diable_existing_loggers': False, 
    'formatters' : {
        'verbose' : {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%y %H:%M:%S"
        },
        'simple' : {
            'format' : '%(levelname)s %(message)s'
        },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG', 
                'class': 'logging.StreamHandler',
            },
        },
        'loggers': {
            'MYAPP': {
                'handlers': ['console'],
                'level': 'DEBUG',
                },            
            },
        }

django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']
import django_on_heroku
import os
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

#AmazonS3 Settings

AWS_ACCESS_KEY_ID = 'AKIAWB743WZLK5BK5EN3'

AWS_SECRET_ACCESS_KEY = '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'

AWS_STORAGE_BUCKET_NAME = 'resume-static2'

AWS_S3_CUSTOM_DOMAIN = 'http://resume-static2.s3.amazonaws.com'

AWS_DEFAULT_ACL = 'public-read'

AWS_S3_OBJECT_PARAMETERS = {
    'cacheControl': 'max-age=86400'
}

AWS_LOCATION = 'static'

AWS_QUERYSTRING_AUTH = False
 
 AWS_HEADERS = {
    'Access-Control-Allow-Origin': '*', 
 }

 DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

 STATICFILES_STORAGE = 'storages.backends.s3boto3.S3StaticStorage'

 STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
 MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

 #End Amazon S3 settings


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
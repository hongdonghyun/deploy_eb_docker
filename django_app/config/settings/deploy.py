from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# AWS settings
AWS_ACCESS_KEY_ID = config_secret_deploy["aws"]["access_key_id"]
AWS_SECRET_ACCESS_KEY = config_secret_deploy["aws"]["secret_access_key"]
AWS_STORAGE_BUCKET_NAME = config_secret_deploy["aws"]["s3_bucket_name"]
AWS_REGION_NAME = config_secret_deploy["aws"]["s3_region"]
S3_USE_SIGV4 = True

STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
STATICFILES_STORAGE = 'config.storages.StaticStorage'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ROOT_DIR, '.static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ROOT_DIR, '.media')
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy["django"]["allowed_hosts"]

# db
DATABASES = config_secret_deploy["django"]["databases"]

print('@@@@@@ DEBUG:', DEBUG)
print('@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)

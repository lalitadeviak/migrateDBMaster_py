import os
import sys

sys.path.append('/home/admin1/migrateDBMaster')
os.environ['DJANGO_SETTINGS_MODULE'] = 'dbmigrate.settings'
os.environ["CELERY_LOADER"] = "django"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
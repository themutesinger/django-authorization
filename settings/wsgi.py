import os

from configurations.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_CONFIGURATION', 'BaseConfig')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

application = get_wsgi_application()

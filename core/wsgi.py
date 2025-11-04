import os
import sys

# Caminho até a pasta do projeto
path = '/home/tertiusupx5/Tertius'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'Tertius.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
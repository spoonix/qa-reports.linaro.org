import sys

# default settings
from kernelcimonitor.settings import *

# general settings
DEBUG = True
ALLOWED_HOSTS = ['*']
STATIC_ROOT = "{{kernelci_monitor_install_base}}/www/static"

# Linaro-specific settings
KERNELCI_URL="https://kernelci.org/"
KERNELCI_API_URL="https://api.kernelci.org/%s/"
KERNELCI_STORAGE_URL="https://storage.kernelci.org/"
KERNELCI_DATE_RANGE=1

SQUADLISTENER_API_URL="http://lava.qa-reports.linaro.org/api/pattern/"

LAVA_XMLRPC_URL="https://validation.linaro.org/RPC2/"

# load secrets from a separate file
from kernelci_monitor_secrets import *
from linaro_ldap import *
SECRET_KEY = open(os.getenv('SECRET_KEY_FILE')).read().strip()
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
	'console': {
	    'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
	    'class': 'logging.StreamHandler',
	    'stream': sys.stdout,
	}
    },
    'loggers': {
	'django': {
	    'handlers': ['console'],
	    'propagate': True,
	    'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
	},
	'': {
	    'handlers': ['console'],
	    'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
	}
    }
}

import os, json
from django.conf import settings


def localSett(BASE_DIR):
    # entorno de desarrollo
    with open("/home/ubunto/prog/json_config/sim52.json") as config_file:
        config = json.load(config_file)
    
    ALLOWED_HOSTS = ['localhost']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'sim52',
        'encuestas',
        'users',
    ]
    
    return config, ALLOWED_HOSTS, INSTALLED_APPS

def prodSett(BASE_DIR):
    # entorno de produccion
    with open("/etc/sim52.json") as config_file:
        config = json.load(config_file)

    ALLOWED_HOSTS = ['localhost', 'url hosting', '172.17.125.17']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'sim52',
        'encuestas',
        'users',
    ]

    RECAPTCHA_PUBLIC_KEY = config['RECAT_PUBLIC_KEY_DEBUG']
    RECAPTCHA_PRIVATE_KEY = config['RECAT_SECRET_KEY_DEBUG']

    return config, ALLOWED_HOSTS, INSTALLED_APPS, RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY


def extensions():
    validExt = ['csv', 'json', 'xlsx', 'pdf', 'html', 'xml', 'sql', 'db', 'py', 'css', 'js']
    validExtPro = ['csv', 'json', 'xlsx', 'xml']
    return validExt, validExtPro


def dbSqlite(BASE_DIR):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'dbs/database.db'),
        }
    }

    return DATABASES
    

def dbmariadb(BASE_DIR):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql', 
            'NAME': 'database',
            'USER': config["MARIADB_USER"],
            'PASSWORD': config["MARIADB_PASSWORD"],
            'HOST': 'localhost',
            'PORT': int(config["MARIADB_PORT"]),
        }
    }
    
    return DATABASES


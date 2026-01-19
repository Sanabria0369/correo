from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'svm-ux'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = [
 'django.contrib.contenttypes',
 'django.contrib.staticfiles',
 'rest_framework',
 'svmapi',
]
MIDDLEWARE = []
ROOT_URLCONF = 'config.urls'
TEMPLATES = []
DATABASES = {'default': {'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

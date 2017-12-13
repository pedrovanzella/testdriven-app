import os
from project import create_app

app = create_app(os.getenv('APP_SETTINGS') or 'default')

import os

class Config():
  CSRF_ENABLED = True
  SECRET = os.getenv('SECRET')
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  TEMPLATE_FOLDER = os.path.join(ROOT_DIR, 'templates')
  APP = None

class DevelopmentConfig(Config):
  DEBUG = True
  IP_HOST = 'localhost'
  PORT_HOST = 8000
  URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST)
  SQLALCHEMY_DATABASE_URI = os.getenv('DB_URL')

class TestingConfig(Config):
  DEBUG = False
  TESTING = True

class ProductionConfig(Config):
  DEBUG = False
  TESTING = False

app_config = {
  'development': DevelopmentConfig(),
  'testing': TestingConfig(),
}

app_active = os.getenv('FLASK_ENV')
if app_active is None:
  app_active = 'development'
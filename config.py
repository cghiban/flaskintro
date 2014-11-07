import os

class BaseConfig(object):
  DEBUG = False
  SECRET_KEY = '\xf8\xcaZ\xa8\xec\xb8 H\xdb+\xbce\x13\x88S?\xe8]@\xa5\x13q1Z'
  #SQLALCHEMY_DATABASE_URI = sqlite:///posts.db
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevelopmentConfig(BaseConfig):
  DEBUG = True

class ProductionConfig(BaseConfig):
  # be explicit ..
  DEBUG = False



import os

class Config():
  SECRET_KEY = os.urandom(64)

  TESTING = True
  DEBUG = True
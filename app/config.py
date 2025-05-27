import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'wR2lWpquF@*-8&)q7lG_2aHAvG$@iM(*13b~^XNURhRDk5rO5~f~Je&mBknC')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///weather.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
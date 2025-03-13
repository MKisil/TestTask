import os


class Config:
    DEBUG = os.getenv('DEBUG') == 'True'
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'default': Config,
    'testing': TestingConfig,
}

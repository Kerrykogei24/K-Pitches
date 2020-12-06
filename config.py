import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:dellakomar24@localhost/kpitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SECRET_KEY = os.environ.get('SECRET_KEY')


    #email configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

pass

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
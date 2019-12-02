import os


basedir = os.path.abspath(os.path.dirname(__file__))


def get_env_var(name):
    try:
        return os.environ[name]
    except KeyError:
        message = f"Expected environment variable {name} not set!"
        raise Exception(message)


POSTGRES_URL = get_env_var('POSTGRES_URL')
POSTGRES_USER = get_env_var('POSTGRES_USER')
POSTGRES_PW = get_env_var('POSTGRES_PW')
POSTGRES_DB = get_env_var('POSTGRES_DB')


class Config:
    SECRET_KEY = get_env_var('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(basedir, 'test.db')}"
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    test=TestingConfig,
)

key = Config.SECRET_KEY

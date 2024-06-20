from decouple import config

DATABASE_URI = config("DATABASE_URL")

if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)

print(DATABASE_URI)

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = config("SECRET_KEY", default="guess-me")
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False
    BCRYTP_LOG_ROUNDS = 13
    WTF_CSRF_ENABLED = True
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTECEPT_REDIRECTS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WTF_CSRF_ENABLED = False 
    DEBUG_TB_ENABLED = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    SQL_ALCHEMY_DATABASE_URI = "sqlite://testdb.sqlite"
    BCRYPT_LOG_ROUNDS = 1
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    DEBUG_TB_ENABLED = False


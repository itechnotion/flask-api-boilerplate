class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = "B\xb2?.\xdf\x9f\xa7m\xf8\x8a%,\xf7\xc4\xfa\x91"
    MONGO_URI="mongodb://localhost:27017/test"
    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"
    SESSION_COOKIE_SECURE = False

class ProductionConfig(Config):
    DEBUG = False
    MONGO_URI="mongodb://localhost:27017/pro"
    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"
    SESSION_COOKIE_SECURE = True

class DevelopmentConfig(Config):
    DEBUG = True   
    MONGO_URI="mongodb://localhost:27017/test"
    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    MONGO_URI="mongodb://localhost:27017/test"
    IMAGE_UPLOADS = "/home/username/projects/my_app/app/static/images/uploads"
    SESSION_COOKIE_SECURE = False
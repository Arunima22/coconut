import os
currentdir = os.path.abspath(os.path.dirname(__file__))

class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class LocalDevelopmentConfig(Config):
	
	SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(currentdir, "coconut_database.sqlite3")
	DEBUG = True

print("config  working good")



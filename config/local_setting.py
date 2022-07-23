from config.base_setting import *

DEBUG = True
SECRET_KEY = "123adam"

SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/seedling_dev?charset=utf8mb4"

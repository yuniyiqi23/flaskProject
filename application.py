from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os

app = Flask(__name__)
manager = Manager(app)

# 配置文件
app.config.from_pyfile("config/base_setting.py")

if "ops_config" in os.environ:
    app.config.from_pyfile("config/%s_setting.py" % os.environ["ops_config"])

# 数据库连接
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost/seedling_dev?charset=utf8mb4"
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL
db = SQLAlchemy(app)

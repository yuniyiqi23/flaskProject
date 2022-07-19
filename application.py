from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 配置文件
app.config.from_pyfile("config/base_setting.py")

# 数据库连接
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost/seedling_dev?charset=utf8mb4"
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL
db = SQLAlchemy(app)

from flask import *
from controllers.user import user_bluepoint as user_bp
from controllers.index import index_bp
from application import app
from flask_debugtoolbar import DebugToolbarExtension
from intercepters.auth import *
from intercepters.error_handles import *

toobar = DebugToolbarExtension(app)

# 注册蓝图
app.register_blueprint(index_bp)
app.register_blueprint(user_bp)



from flask import *
from controllers.user import user_bluepoint
from application import app

# 注册蓝图
app.register_blueprint(user_bluepoint)


@app.route('/')
def index():
    return 'index.html'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        flash('You were successfully logged in')
        return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.errorhandler(404)
def not_found():
    return render_template('error.html'), 404

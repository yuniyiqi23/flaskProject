from flask import *

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'GET':
        flash('You were successfully logged in')
        return redirect(url_for('index'))
    return render_template('login.html', error=error)


from application import app


@app.errorhandler(404)
def not_found(e):
    return "not_found"

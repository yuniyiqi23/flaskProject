from application import app


@app.before_request
def before_request():
    app.logger.info("---------before_request----------")


@app.after_request
def after_request(response):
    app.logger.info("---------after_request----------")
    return response


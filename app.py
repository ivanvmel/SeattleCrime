import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import send_from_directory

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    handler = RotatingFileHandler('SeattleCrime.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
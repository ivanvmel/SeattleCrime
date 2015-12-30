import logging
import os
from logging.handlers import RotatingFileHandler
from flask import Flask
from flask import send_from_directory

app = Flask(__name__, static_url_path='')

@app.route("/")
def index():
    return app.send_static_file('index.html')

if __name__ == "__main__":
    handler = RotatingFileHandler('SeattleCrime.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()
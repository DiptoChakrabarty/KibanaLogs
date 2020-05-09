from flask import Flask
import logging

app = Flask(__name__)

from logging.config import fileConfig

fileConfig('logging.cfg')

@app.route("/")
def home():
    app.logger.info("Process default Request")
    return "logging application"



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
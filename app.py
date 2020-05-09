from flask import Flask
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG,
        filename="app.log",
        format='%(asctime)s %(levelname)s-%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')

@app.route("/")
def home():
    app.logger.info("Process default Request")
    return "logging application"



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
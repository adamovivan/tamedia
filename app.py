from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Tamedia from Ivan Adamov'


app.run(host="0.0.0.0", port=11130)

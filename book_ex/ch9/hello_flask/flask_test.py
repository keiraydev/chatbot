from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/info')
def info():
    return 'Info'


@app.route('/hello')
def hello():
    return {
        "answer": "hello",
        "Intent": "인사"
    }


# $ export FLASK_APP=hello.py
# $ export FLASK_ENV=development
# $ flask run

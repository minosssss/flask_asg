import os
from flask import Flask, app
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
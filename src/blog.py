__author__ = 'Dario Coco'

from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True
app.secret_key = "12345"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'

login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/login")
def login():
    return render_template('login.html')

@login_manager.user_loader
def load_user():
    pass

def init_db():
    db.create_all()

if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app.auth.views import auth_blueprint
from app.book.views import book_blueprint

app.register_blueprint(auth_blueprint)
app.register_blueprint(book_blueprint)

@login_manager.user_loader
def load_user(user_id):
    from app.auth.models import User
    return User.query.get(user_id)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

import email_validator
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "123456"
Bootstrap(app)
class MyForm(FlaskForm):
    email = StringField('email', validators=[validators.Email(message='That\'s not a valid email address.')])
    password = PasswordField('password', validators=[validators.Length(min=8)])
    submit = SubmitField('Login')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@email.com' and form.password.data == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
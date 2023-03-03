from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=1, max=100)])
    rating = StringField('Rating', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Add Book')

class EditBookForm(FlaskForm):
    rating = StringField('Rating', validators=[DataRequired(), Length(min=1, max=100)])
    submit = SubmitField('Update Book')
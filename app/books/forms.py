from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class AddBookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()], description="Enter title...")
    author = StringField('Book author', validators=[DataRequired()], description="Enter author...")
    genre = SelectField('Book genre')
    submit = SubmitField('Add book')


class UpdateBookForm(FlaskForm):
    title = StringField('Book title', validators=[DataRequired()], description="Enter title...")
    author = StringField('Book author', validators=[DataRequired()], description="Enter author...")
    genre = SelectField('Book genre')

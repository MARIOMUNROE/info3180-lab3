from flask_wtf import FlaskForm
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
	name = StringField("Username", validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	subject = StringField("Subject", validators=[DataRequired()])
	message = TextField("Message", validators=[DataRequired()])
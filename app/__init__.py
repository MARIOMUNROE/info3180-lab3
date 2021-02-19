from flask import Flask
from flask_mail import Mail
from .config import Config
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] ='somesecretkey'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL PORT']= '465'
app.config['MAIL_USERNAME']='dc65d868bd8845'
app.config['MAIL_PASSWORD']='e5cdb9e774aae3'

mail = Mail(app)
from app import views
csrf.init_app(app)
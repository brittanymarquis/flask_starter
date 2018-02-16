from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY']='enter some random passphase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '908f11bafc78eb'
app.config['MAIL_PASSWORD'] = 'fc923bb07a2f90'

mail = Mail(app)
from app import views
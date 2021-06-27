"""Data models."""
from application.__init__ import db
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length


class User(UserMixin, db.Model):
    __tablename__: 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

    # def __init__(self, username, email, password):
    #     self.id = id
    #     self.username = username
    #     self.email = email
    #     self.password = password

    def __repr__(self):
        return f"User('{self.id}', '{self.username}', '{self.email}','{self.password})"


class LoginForm(FlaskForm):
    __tablename__: 'loginForm'
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')


class RegisterForm(FlaskForm):
    __tablename__: 'registerForm'
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
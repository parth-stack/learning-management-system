from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from target.models import User

class RegisterForm(FlaskForm):
    username = StringField('name', validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(5)])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up') 
    def validate_username(self,n):
        user=User.query.filter_by(username=n.data).first()
        if user:
            raise ValidationError('the username is taken please choose a different one')
    def validate_email(self,e):
        user=User.query.filter_by(email=e.data).first()
        if user:
            raise ValidationError('the email is taken please choose a different one')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')
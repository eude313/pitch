from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Length, Required, EqualTo, Email, ValidationError
from webapp.models import User
from flask_login import current_user

class registrationForm(FlaskForm):
    email = StringField('Your email',validators=[Required(),Email()])
    username = StringField(' username',validators = [Required(), Length(min=2, max=22)])
    password = PasswordField('Password',validators = [Required(), Length(min=3, max=20) ])
    confirm_password = PasswordField('Confirm Password',validators = [Required(), EqualTo('confirm_password',message = 'Passwords must match')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('username exists please use another one')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
           raise ValidationError('email exists please use another one')
            
class loginForm(FlaskForm):
    email = StringField('Your Email',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
    
class Update_AccountForm(FlaskForm):
    email = StringField('Your email',validators=[Required(),Email()])
    username = StringField(' username',validators = [Required(), Length(min=2, max=22)])
    picture = FileField('Update profile picture',validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update profile')
    
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('username exists please use another one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
             raise ValidationError('email exists please use another one')
            
    
class blog_form(FlaskForm):
    title = StringField('Title',validators=[Required()])
    content = TextAreaField('content',validators=[Required()])
    submit = SubmitField('post')
    
    
from . import auth
from webapp import db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from ..models import User
from flask import  render_template,url_for, flash, redirect
from .forms import registrationForm, loginForm

@auth.route('/signup', methods=['POST', 'GET'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = registrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to login ', 'success')
        return redirect(url_for('auth.signIn'))
    return render_template('signUp.html', form= form, title='signUp')

@auth.route("/login", methods=['POST', 'GET'])
def signIn():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = loginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
           login_user(user, remember=form.remember.data)
           return redirect(url_for('main.home')) 
        else:
            flash('login unsuccessful. please check your email or password.', 'danger')
    return render_template('signIn.html', form= form, title="signIn")

@auth.route("/logout")
def signOut():
    logout_user()
    return redirect(url_for('main.home')) 

@auth.route("/account")
@login_required
def Account():
    image_file = url_for('static',filename='/images/')
    return render_template('Profile.html',  title="Profile", image_file= image_file)
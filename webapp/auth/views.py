from . import auth
from webapp import db, bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from ..models import User, Post
from flask import render_template, url_for, flash, redirect
from .forms import blog_form, registrationForm, loginForm

@auth.route('/signup', methods=['POST', 'GET'])
def signUp():
    if current_user.is_authenticated:
        return redirect(url_for('auth.signUp'))
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


@auth.route('/blogs')
def blogs():
    posts= Post.query.all()
    return render_template('blogs.html', posts=posts)

@auth.route('/post/new', methods=['POST', 'GET'])
@login_required
def post():
    form =blog_form()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash( " post has been created", "success" )
        return redirect(url_for('auth.blogs'))
    return render_template('post.html',form=form)

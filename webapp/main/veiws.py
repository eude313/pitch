from . import main
from flask import render_template, url_for

# landing page
@main.route('/')
def home():
    return render_template('index.html')


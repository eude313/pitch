from . import main
from flask import render_template

# landing page
@main.route('/')
def home():
    return render_template('index.html')


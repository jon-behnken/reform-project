import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

landing = Blueprint('landing', __name__, url_prefix='/')

@landing.route('/', methods=['GET', 'POST'])
def hello():
    return render_template('home.html')

from reform import app
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

about_bp = Blueprint('about', __name__, url_prefix='/about')

@about_bp.route('/', methods=['GET', 'POST'])
def show_about():
  return render_template('about.html')

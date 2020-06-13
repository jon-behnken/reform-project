import functools
from powertools.main import generate_datatable_JSON

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, current_app
)

from reform import app

search = Blueprint('search', __name__, url_prefix='/search')

@search.route('/', methods=['GET', 'POST'])
def show_search():
    return render_template('search.html')

@search.route('/t/<topicQueryString>', methods=['GET', 'POST'])
def generate_JSON(topicQueryString):
    propublica_api_key = app.config['PROPUBLICA_API_KEY']
    DataTable_data = generate_datatable_JSON(propublica_api_key, topicQueryString)
    return DataTable_data

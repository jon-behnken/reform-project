from powertools.main import generate_datatable_JSON

from flask import (
    Blueprint,
    render_template,
    current_app,
)

search = Blueprint("search", __name__, url_prefix="/search")


@search.route("/", methods=["GET", "POST"])
def show_search():
    return render_template("search.html")


@search.route("/t/<topicQueryString>", methods=["GET", "POST"])
def generate_JSON(topicQueryString):
    propublica_api_key = current_app.config["PROPUBLICA_API_KEY"]
    DataTable_data = generate_datatable_JSON(propublica_api_key, topicQueryString)
    return DataTable_data

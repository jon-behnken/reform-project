from flask import (
    Blueprint,
    render_template,
)

landing = Blueprint("landing", __name__, url_prefix="/")


@landing.route("/", methods=["GET", "POST"])
def hello():
    return render_template("home.html")

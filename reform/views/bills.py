import json
from powertools.main import (
    generate_bill_data,
    generate_bill_fulltext,
    get_members_by_state,
    get_member_by_id,
)
from flask import (
    Blueprint,
    render_template,
    current_app,
)

bill = Blueprint("bill", __name__, url_prefix="/bill")


@bill.route("/<bill_id>", methods=["GET", "POST"])
def show_bill(bill_id):
    propublica_api_key = current_app.config["PROPUBLICA_API_KEY"]
    govtrack_api_key = current_app.config["GOVTRACK_API_KEY"]
    bill_data = generate_bill_data(propublica_api_key, bill_id)
    bill_type = bill_data[0]["bill_type"]
    bill_number = bill_data[0]["number"].split(".")[-1]
    bill_fulltext = generate_bill_fulltext(govtrack_api_key, bill_type, bill_number)

    bill_title = bill_data[0]["short_title"]
    bill_intro_date = bill_data[0]["introduced_date"]
    # bill_summary = bill_data[0]["summary"]
    bill_history = bill_data[0]["actions"]
    bill_sponsor_data = get_member_by_id(propublica_api_key, bill_data[0]["sponsor_id"])
    bill_sponsor_twitter = bill_sponsor_data[0]["twitter_account"]
    bill_sponsor_contact_url = bill_sponsor_data[0]["contact_url"]
    bill_sponsor_json = json.dumps(
        [
            {
                "sponsor_id": bill_data[0]["sponsor_id"],
                "sponsor": bill_data[0]["sponsor"],
                "sponsor_party": bill_data[0]["sponsor_party"],
                "sponsor_state": bill_data[0]["sponsor_state"],
                "sponsor_uri": bill_data[0]["sponsor_uri"],
                "sponsor_twitter": bill_sponsor_twitter,
                "sponsor_contact_url": bill_sponsor_contact_url,
            }
        ]
    )
    # bill_votes = bill_data[0]["votes"]
    return render_template(
        "bills.html",
        bill_title=bill_title,
        bill_intro_date=bill_intro_date,
        bill_history=bill_history,
        bill_fulltext=bill_fulltext,
        bill_sponsor=bill_sponsor_json,
    )


@bill.route("/<bill_id>/history", methods=["GET", "POST"])
def get_bill_history(bill_id):
    api_key = current_app.config["PROPUBLICA_API_KEY"]
    bill_data = generate_bill_data(api_key, bill_id)
    bill_history = bill_data[0]["actions"]
    return json.dumps(bill_history)


@bill.route("/members/all/<state_id>", methods=["GET", "POST"])
def get_all_members(state_id):
    api_key = current_app.config["PROPUBLICA_API_KEY"]
    all_members = get_members_by_state(api_key, state_id)
    return json.dumps(all_members)

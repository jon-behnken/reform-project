import requests
import json
import yaml
import os
from bs4 import BeautifulSoup

# set URLS for APIs
proPublica_DataTable_url = (
    "https://api.propublica.org/congress/v1/bills/search.json?query={}&sort=date"
)
proPublica_bill_url = "https://api.propublica.org/congress/v1/116/bills/{}.json"

proPublica_SENATE_member_url = (
    "https://api.propublica.org/congress/v1/members/{}/{}/current.json"
)
proPublica_SENATE_member_id_url = (
    "https://api.propublica.org/congress/v1/members/{}.json"
)
proPublica_HOUSE_member_url = "https://api.propublica.org/congress/v1/members/{chamber}/{state}/{district}/current.json"

govtrack_bill_url = "https://www.govinfo.gov/link/bills/116/{}/{}?link-type=html"


def generate_datatable_JSON(api_key, topicQueryString):
    proPublica_DataTable_request_url = proPublica_DataTable_url.format(topicQueryString)
    response = requests.get(
        proPublica_DataTable_request_url, headers={"X-API-KEY": api_key}
    )
    return response, json.dumps(response.json()["results"][0]["bills"])


def generate_bill_data(api_key, bill_slug):
    proPublica_bill_url_slug = proPublica_bill_url.format(bill_slug)
    response = requests.get(proPublica_bill_url_slug, headers={"X-API-KEY": api_key})
    return response, response.json()["results"]


def generate_bill_fulltext(api_key, bill_type, bill_number):
    govtrack_bill_url_formatted = govtrack_bill_url.format(bill_type, bill_number)
    response = requests.get(govtrack_bill_url_formatted)
    soup = BeautifulSoup(response.text, features="html.parser")

    soupTitle = soup.find("title")
    if soupTitle and "Service Error" in soupTitle.text:
        return "There was an error fetching the bill's full text. It could be this bill is too recent, or another error with GovTrack."

    return response, response.text


def get_contact_form_url(member_id):
    member_file = "{}.yaml".format(member_id)
    yaml_file = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "yaml", member_file)
    )
    with open(yaml_file, "r") as stream:
        yaml_data = yaml.safe_load(stream)

    return yaml_data["contact_form"]["steps"][0]["visit"]


def get_members_by_state(api_key, member_state):
    senate_members_formatted_url = proPublica_SENATE_member_url.format(
        "senate", member_state
    )
    response = requests.get(
        senate_members_formatted_url, headers={"X-API-KEY": api_key}
    )
    response_with_contact = []
    for i in response.json()["results"]:
        member_id = i["id"]
        contact_url = get_contact_form_url(member_id)
        i["contact_url"] = contact_url
        response_with_contact.append(i)
    return response, response_with_contact


def get_member_by_id(api_key, member_id):
    senate_member_by_id_url = proPublica_SENATE_member_id_url.format(member_id)
    response = requests.get(senate_member_by_id_url, headers={"X-API-KEY": api_key})
    response_with_contact = []
    for i in response.json()["results"]:
        member_id = i["id"]
        contact_url = get_contact_form_url(member_id)
        i["contact_url"] = contact_url
        response_with_contact.append(i)
    return response, response_with_contact

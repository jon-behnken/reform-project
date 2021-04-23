# Track The Change

  

Track The Change is a web application that aims to consolidate information about bills before the United States Congress with contact information

for legislative representatives. Track The Change aims to bolster the ongoing advocacy movement to reform policing and the criminal justice system in the United States.

To that end, Track The Change selectively highlights bills whose proposals are consequential to these policy areas.

  

## The Application

  

TTC is a Flask application that uses `waitress` as its webserver. I create and initialize the application using a factory method so that testing the application is easier. To access the application in Blueprints, use Flask's `current_app` built-in.

  

## Testing

  

The tests are located in the `tests` folder. To test the backend functions that generate the data, I use Python's `unittest`. To run the unit tests, you run the script as a module so it is able to import the powertool functions. For instance:

  

> \>>> ~/reform-project> python -m tests.test_powertools

  

## Views

  

Currently TTC has two main views -- the search view and the bills view. Both views are fairly straightforward.

### Search
- **Accessed by:** front-end
- **Arguments:** str
- **Returns:** JSON

  

Using jQuery, the `topic-select` element is bound to a function that passes the search view its value -- a string from the that represents a topic to search the ProPublica bill database. Currently the search system is very rudimentary but future updates will provide more nuanced, accurate and complex filtering to curate the dataset. The view function returns JSON data that is passed back to the jQuery success callback and used to populate a DataTable.

  

### Bills

  

`show_bill(bill_id)`
- **Accessed by:** front-end
- **Arguments:** str
- **Returns**: renders a Flask template

  

Each row in the DataTable rendered by the `search` view contains a URL that references this view function. The `bill_id` is passed as URL parameter and the function uses ProPublica to gather most of the metadata information about the bill and GovTrack to pull the full text of the bill. This view function returns a Flask template with several variables containing the appropriate bill's information.

  

`get_bill_history(bill_id)`
- **Accessed by:** front-end
- **Arguments:** str
- **Returns**: JSON

  

This view function uses the ProPublica API to generate a history of votes and actions on the bill and returns it in JSON data.

  

`get_all_members(state_id)`
- **Accessed by:** front-end
- **Arguments:** str
- **Returns**: JSON

  

This view function uses the ProPublica API to generate a JSON object with information on senators for a specific state.
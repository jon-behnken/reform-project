from flask import Flask, request, render_template
from multiprocessing import Process
from flask_sqlalchemy import SQLAlchemy
import logging
from datetime import datetime
from logging.handlers import RotatingFileHandler

# initate app
app = Flask(__name__)
app.config.from_pyfile('../config.py')


# test_config = None
# if test_config is None:
#     # load the instance config, if it exists, when not testing
#     app.config.from_pyfile('../config.py', silent=True)
# else:
#     # load the test config if passed in
#     app.config.from_mapping(test_config)

@app.before_first_request
def setup_logging():
    fh = logging.FileHandler('../logging/reform_app_' + datetime.strftime(datetime.now(), "%Y.%m.%d") + '.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(message)s')
    fh.setFormatter(formatter)
    app.logger.addHandler(fh)

@app.after_request
def log_activity(response):
    message = [request.remote_addr, request.method, request.path, str(response.status_code)]
    message = ' | '.join(message)
    app.logger.info(message)
    return response

#import views
from views.landing import landing
from views.search import search
from views.bills import bill

#register views
app.register_blueprint(landing)
app.register_blueprint(search)
app.register_blueprint(bill)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

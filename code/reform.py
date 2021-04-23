from flask import Flask, request
import logging
import os
from datetime import datetime


def create_app(test_config=None):
    # initate app
    app = Flask(__name__)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("../config.py")
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # set up app logger before first request
    @app.before_first_request
    def setup_logging():
        log_file = os.path.join(
            app.config["BASE_DIR"],
            "logs",
            "app_factory_" + datetime.strftime(datetime.now(), "%Y.%m.%d") + ".log",
        )
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s | %(message)s")
        fh.setFormatter(formatter)
        app.logger.addHandler(fh)

    @app.after_request
    def log_activity(response):
        message = [
            request.remote_addr,
            request.method,
            request.path,
            str(response.status_code),
        ]
        message = " | ".join(message)
        app.logger.info(message)
        return response

    # import views
    from views.landing import landing
    from views.search import search
    from views.bills import bill
    from views.about import about_bp

    # register views
    app.register_blueprint(landing)
    app.register_blueprint(search)
    app.register_blueprint(bill)
    app.register_blueprint(about_bp)

    return app

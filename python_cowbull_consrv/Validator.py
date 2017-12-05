from flask import Flask
from helpers.ErrorHandler import ErrorHandler


class Validator(object):
    def __init__(self):
        self.error_handler = None

    def check_readiness(self, app=None):
        if app is None:
            raise ValueError("The Flask app must be passed to the Configurator")
        if not isinstance(app, Flask):
            raise TypeError("Expected a Flask object")

        self.error_handler = ErrorHandler(
            module="Validator",
            method="check_readiness",
            level=app.config["logging_level"],
            format=app.config["logging_format"]
        )

        readiness_url = "{}:{}/{}/{}".format(
            app.config.get("cowbull_server"),
            app.config.get("cowbull_port"),
            app.config.get("cowbull_game_version"),
            app.config.get("cowbull_ready_route")
        )

        self.error_handler.log(message="Checking readiness at: {}".format(readiness_url))

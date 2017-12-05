from flask import Flask
from helpers.ErrorHandler import ErrorHandler
import requests


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

        retries = app.config.get("cowbull_tolerance", 3)

        self.error_handler.log(message="Checking readiness at: {}".format(readiness_url))
        success_sentinel = False

        for i in range(0, retries):
            try:
                _headers = {"Content-type": "application/json"}
                r = requests.get(readiness_url, timeout=0.5, headers=_headers)
                if r.status_code == 200:
                    self.error_handler.log(message="{} reports ready (status 200)".format(readiness_url))
                    success_sentinel = True
                    break
                #else:
                #    raise ConnectionError()
            except Exception as e:
                self.error_handler.log(message="{} reports: {} --- retrying {} of {}".format(
                    readiness_url,
                    repr(e),
                    i + 1,
                    retries
                ))

        return success_sentinel

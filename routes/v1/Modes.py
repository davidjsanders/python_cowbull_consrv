from flask.views import MethodView
from flask import request
from helpers.build_response import build_response
from helpers.html_error_handler import html_error_handler
from python_cowbull_consrv import app
import json
import requests


class Modes(MethodView):
    @property
    def response(self):
        return dict(server=None, status=None, ads=[], highscores=[])

    @property
    def modes_url(self):
        return "{}:{}/{}/modes".format(
            app.config.get("cowbull_server", "localhost"),
            app.config.get("cowbull_port", 5000),
            app.config.get("cowbull_game_version", "v1")
        )

    @property
    def headers(self):
        return {
            "Content-type": "application/json"
        }

    def get(self):
        try:
            r = requests.get(
                url="{}".format(self.modes_url),
                timeout=app.config.get("cowbull_timeout"),
                headers=self.headers
            )
        except Exception as e:
            return html_error_handler(
                html_status=500,
                html_exception=repr(e),
                html_message="An exception occurred while accessing the game service modes.",
                html_module="Modes.py",
                html_method="get"
            )

        _response = self.response
        if r.status_code in [200, 400, 500]:
            _response["server"] = r.json()
            _response["status"] = r.status_code
        else:
            # TODO Circuit breaker
            return html_error_handler(
                html_status=r.status_code,
                html_message=r.text,
                html_exception="Error occurred while fetching a new game",
                html_module="Game.py",
                html_method="get"
            )

        return build_response(response_data=_response, html_status=r.status_code)


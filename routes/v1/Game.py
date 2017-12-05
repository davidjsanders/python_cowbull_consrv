from flask.views import MethodView
from flask import request
from helpers.build_response import build_response
from helpers.html_error_handler import html_error_handler
from python_cowbull_consrv import app
import json
import requests


class Game(MethodView):
    @property
    def response(self):
        return dict(server=None, status=None, ads=[], highscores=[])

    @property
    def game_url(self):
        return "{}:{}/{}/game".format(
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
        mode = request.args.get('mode', "Normal")
        try:
            r = requests.get(
                url="{}?mode={}".format(self.game_url, mode),
                timeout=app.config.get("cowbull_timeout"),
                headers=self.headers
            )
        except Exception as e:
            return html_error_handler(
                html_status=500,
                html_exception=repr(e),
                html_message="An exception occurred while accessing the game service.",
                html_module="Game.py",
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

    def post(self, gamekey=None):
        if not gamekey:
            return html_error_handler(
                html_status=400,
                html_message="The game key must be provided",
                html_exception="No game key",
                html_module="Game.py",
                html_method="post"
            )

        try:
            user_data = request.get_json()
            digits = user_data["digits"]
        except KeyError as ke:
            return html_error_handler(
                html_status=400,
                html_message="There were no digits found in the request's JSON data. "
                             "Are you sure they were provided AND that the header was "
                             "passed as content-type:application/json?",
                html_exception="No digits in the data",
                html_module="Game.py",
                html_method="post"
            )

        except Exception as e:
            return html_error_handler(
                html_status=400,
                html_message="There was no JSON data found in the request. Are you "
                             "sure it was provided AND that the header was passed "
                             "as content-type:application/json?",
                html_exception="No JSON data could be found with the request",
                html_module="Game.py",
                html_method="post"
            )

        payload = {
            "key": gamekey,
            "digits": digits
        }

        try:
            r = requests.post(
                url="{}".format(self.game_url),
                data=json.dumps(payload),
                timeout=app.config.get("cowbull_timeout"),
                headers=self.headers
            )
        except Exception as e:
            return html_error_handler(
                html_status=500,
                html_exception=repr(e),
                html_message="An exception occurred while accessing the game service.",
                html_module="Game.py",
                html_method="get"
            )
        _response = self.response

        if r.status_code in [200, 201, 400, 500]:
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

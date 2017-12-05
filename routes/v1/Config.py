from flask.views import MethodView
from helpers.build_response import build_response
from python_cowbull_consrv import app
from python_cowbull_consrv import load_env


class Config(MethodView):
    def get(self, env=None):
        if not env:
            _response = {
                "action": "get",
                "configuration": {
                    "cowbull_server": app.config.get("COWBULL_SERVER", "localhost"),
                    "cowbull_port": app.config.get("COWBULL_PORT", 5000),
                    "cowbull_game_version": app.config.get("COWBULL_GAME_VERSION", "v1")
                }
            }
        else:
            _response = {
                "action": "get one",
                "configuration": {
                    env: app.config.get(env, "unknown")
                }
            }
        _status = 200

        return build_response(response_data=_response, html_status=_status)

    def post(self):
        load_env(app=app)
        _response = {
            "action": "reload",
            "configuration": {
                "cowbull_server": app.config.get("COWBULL_SERVER", "localhost"),
                "cowbull_port": app.config.get("COWBULL_PORT", 5000),
                "cowbull_game_version": app.config.get("COWBULL_GAME_VERSION", "v1")
            }
        }
        _status = 200

        return build_response(response_data=_response, html_status=_status)

    def put(self):
        _response = {
            "config put": "wip"
        }
        _status = 200

        return build_response(response_data=_response, html_status=_status)

    def delete(self):
        _response = {
            "config delete": "wip"
        }
        _status = 200

        return build_response(response_data=_response, html_status=_status)

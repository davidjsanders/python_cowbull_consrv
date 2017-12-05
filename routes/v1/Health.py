from flask.views import MethodView
from helpers.build_response import build_response


class Health(MethodView):
    def get(self):
        #
        # TODO: Add some health checking criteria, probably verifying server_url connections.
        #
        _response = {
            "health": "ok"
        }
        _status = 200

        return build_response(response_data=_response, html_status=_status)

from flask.views import MethodView
from helpers.build_response import build_response


class Readiness(MethodView):
    def get(self):
        #
        # TODO: Add readiness checking
        #
        return build_response(
            html_status=200,
            response_data={"status": "ready"},
            response_mimetype="application/json"
        )

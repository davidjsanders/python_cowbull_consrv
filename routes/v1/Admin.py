from flask.views import MethodView
from flask import request
from helpers.build_response import build_response


class Admin(MethodView):
    def __init__(self):
        pass

    def get(self):
        return build_response(
            html_status=200,
            response_data={
                "method": "get",
                "status": "work in progress"
            },
            response_mimetype="application/json"
        )

    def post(self):
        return build_response(
            html_status=200,
            response_data={
                "method": "post",
                "status": "work in progress"
            },
            response_mimetype="application/json"
        )

    def put(self):
        return build_response(
            html_status=200,
            response_data={
                "method": "put",
                "status": "work in progress"
            },
            response_mimetype="application/json"
        )

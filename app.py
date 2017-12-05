from python_cowbull_consrv import app, configurator
from helpers.html_error_handler import html_error_handler
from routes.v1routes import v1routes

# Add cross origin scripting support
# ----------------------------------
@app.after_request
def allow_cors(resp):
    resp.headers.add('Access-Control-Allow-Origin', '*')
    resp.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return resp

@app.errorhandler(404)
def page_not_found(e):
    return html_error_handler(
        html_status=404,
        html_exception="A 404 (not found) error occurred.",
        html_message="The resource requested was not found."
    )

@app.errorhandler(405)
def page_not_found(e):
    return html_error_handler(
        html_status=405,
        html_exception="Bad method request",
        html_message="The resource requested does not support the method used in the call."
    )

v1routes(app=app)

if __name__ == "__main__":
    configurator.dump_variables()
    app.run\
        (
            host=app.config.get("FLASK_HOST", app.config.get("flask_host", "0.0.0.0")),
            port=app.config.get("FLASK_PORT", app.config.get("flask_port", 5000)),
            debug=app.config.get("FLASK_DEBUG", app.config.get("flask_debug", True)),
        )

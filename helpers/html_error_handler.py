from helpers.build_response import build_response


def html_error_handler(
        html_status=None,
        html_exception=None,
        html_message=None,
        html_module=None,
        html_method=None
):
    response_dict = {
        "status": "error",
        "module": html_module or "NA",
        "method": html_method or "NA",
        "exception": html_exception or "An exception occurred.",
        "message": html_message or "Oops! An error has occurred and not been caught! It has been logged."
    }
    return build_response(
        response_data=response_dict,
        html_status=html_status
    )

import os


def load_env(app=None):
    cowbull_server = os.environ.get(
        "COWBULL_SERVER",
        os.environ.get(
            "cowbull_server", "localhost"
        )
    )
    if cowbull_server and len(cowbull_server) >= 7:
        if cowbull_server[0:7] not in ["http://", "https:/"]:
            cowbull_server = "http://{}".format(cowbull_server)
    app.config["cowbull_server"] = cowbull_server

    app.config["cowbull_port"] = int(os.environ.get(
        "COWBULL_PORT",
        os.environ.get(
            "cowbull_port",
            5000
        )
    ))

    app.config["cowbull_game_version"] = os.environ.get(
        "COWBULL_GAME_VERSION",
        os.environ.get(
            "cowbull_game_version",
            "v1"
        )
    )

    app.config["cowbull_timeout"] = int(
        os.environ.get(
            "COWBULL_TIMEOUT",
            os.environ.get(
                "cowbull_timeout",
                1
            )
        )
    )
#############################################################################
# Version 1 routes                                                          #
#############################################################################

from routes.v1.Readiness import Readiness
from routes.v1.Health import Health
from routes.v1.Game import Game
from routes.v1.Modes import Modes
from routes.v1.Config import Config


def v1routes(app=None):
    if app is None:
        raise ValueError("App must be passed to the route object!")
    version = "v1"

    # Define views
    game_view = Game.as_view('Game')
    mode_view = Modes.as_view('Modes')
    config_view = Config.as_view('Config')
    health_view = Health.as_view('Health')
    hv2 = Health.as_view('Health2')
    readiness_view = Readiness.as_view('ready')

    # Add URL rules
    app.add_url_rule(
        '/{}/game'.format(version),
        view_func=game_view,
        methods=["GET"]
    )

    app.add_url_rule(
        '/{}/game/<gamekey>'.format(version),
        view_func=game_view,
        methods=["POST"]
    )

    app.add_url_rule(
        '/{}/modes'.format(version),
        view_func=mode_view,
        methods=["GET"]
    )

    app.add_url_rule(
        '/{}/config/<env>'.format(version),
        view_func=config_view,
        methods=["GET"]
    )

    app.add_url_rule(
        '/{}/config'.format(version),
        view_func=config_view,
        methods=["GET", "POST"]
    )

    app.add_url_rule(
        '/{}/health'.format(version),
        view_func=health_view,
        methods=["GET"]
    )

    app.add_url_rule(
        '/_ah/health',
        view_func=health_view,
        methods=["GET"]
    )

    app.add_url_rule(
        '/{}/ready'.format(version),
        view_func=readiness_view,
        methods=["GET"]
    )

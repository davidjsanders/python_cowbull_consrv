from flask import Flask
from python_cowbull_consrv.Configurator import Configurator
from python_cowbull_consrv.Validator import Validator
from datetime import datetime

app = Flask(__name__)
configurator = Configurator()
configurator.execute_load(app=app)

validator = Validator()
app.config["cowbull_ready"] = validator.check_readiness(app=app)
app.config["cowbull_ready_checked_at"] = datetime.utcnow()

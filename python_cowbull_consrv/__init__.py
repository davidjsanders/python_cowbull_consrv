from flask import Flask
from python_cowbull_consrv.Configurator import Configurator
from python_cowbull_consrv.Validator import Validator

app = Flask(__name__)
configurator = Configurator()
configurator.execute_load(app=app)

validator = Validator()
validator.check_readiness(app=app)

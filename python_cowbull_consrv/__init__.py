from flask import Flask
from python_cowbull_consrv.load_env import load_env
from python_cowbull_consrv.Configurator import Configurator

app = Flask(__name__)
c = Configurator()
c.execute_load(app=app)
#load_env(app)

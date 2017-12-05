from flask import Flask
from python_cowbull_consrv.load_env import load_env

app = Flask(__name__)
load_env(app)

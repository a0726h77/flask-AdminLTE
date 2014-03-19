# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask
app = Flask('project')
app.debug = True

# import controllers
from project.controllers import *

# import model
from models.models import db


#### initial logger ####
import logging
from logging.handlers import RotatingFileHandler
import os

LOG_PATH = '/'.join((os.path.dirname(os.path.realpath(__file__)), 'log'))
if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

handler = RotatingFileHandler(LOG_PATH + '/debug.log', maxBytes=10000, backupCount=1)
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)
#### initial logger ####


#### initial sesion ####
from datetime import timedelta
app.config['SECRET_KEY'] = 'random'
app.permanent_session_lifetime = timedelta(seconds=60*60*10)  # session expire time
#### initial sesion ####


#### initial database ####
app.config.from_pyfile('config/database.cfg')
db.init_app(app)
#### initial database ####


#### router ####
from werkzeug.routing import Rule

urlpatterns = {
    Rule('/', endpoint='index'),
}

for rule in urlpatterns:
    app.url_map.add(rule)
#### router ####

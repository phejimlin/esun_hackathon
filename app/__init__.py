# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)

#Configuration of application, see configuration.py, choose one and uncomment.
#app.config.from_object('configuration.ProductionConfig')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jim@esunmysql:1QAZ2wsx3edc@esunmysql.mysql.database.azure.com/esun'
app.config.from_object('app.configuration.DevelopmentConfig')
#app.config.from_object('configuration.TestingConfig')

Bootstrap(app) #flask-bootstrap
db = SQLAlchemy(app) #flask-sqlalchemy

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'

app.secret_key = 'x88=B\xdeJHP\xce\x17\x0f\x16\xe7\xaf\xcf\xf2J!b\xa8{\xbcc\xe8j'

from app import views, models

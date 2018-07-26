#WebApi/v1/application.wsgi
import importlib
import os, sys

sys.path.insert(0, "/home/pi/RaspDataLogger/DataloggerWebApp/WebApi/v1")

import bottle
from requestlogger import WSGILogger, ApacheFormatter
from logging import FileHandler
from bottle.ext import sqlite

application = bottle.default_app()

pluginSqlite = sqlite.Plugin(dbfile='/home/pi/RaspDataLogger/appdb/app.db')
application.install(pluginSqlite)

import web_api_service

handlers = [FileHandler("/home/pi/RaspDataLogger/DataloggerWebApp/WebApi/v1/logs/v1_restapi.log"),]

application = WSGILogger(application, handlers, ApacheFormatter())

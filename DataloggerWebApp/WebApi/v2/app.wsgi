#AppWebSrv/appsrv_v1/application.wsgi
import importlib
import os, sys

sys.path.insert(0, "/home/pi/MeterWebApp/AppWebSrv/appsrv_v1")

import bottle
from requestlogger import WSGILogger, ApacheFormatter
from logging import FileHandler

application = bottle.default_app()

import appserv_config_api

handlers = [FileHandler("/home/pi/MeterWebApp/AppWebSrv/appsrv_v1/logs/appservice.log"),]

application = WSGILogger(application, handlers, ApacheFormatter())

#WebApi/v1/application.wsgi
import importlib
import os, sys

sys.path.insert(0, "home/pi/RaspDataLogger/DataloggerWebApp/WebApi/v1")

import bottle
from requestlogger import WSGILogger, ApacheFormatter
from logging import FileHandler

application = bottle.default_app()

import web_api_service

handlers = [FileHandler("/home/pi/RaspDataLogger/DataloggerWebApp/WebApi/v1/logs/v1_restapi.log"),]

application = WSGILogger(application, handlers, ApacheFormatter())

#bottle.run(application, host='localhost', port=8080)

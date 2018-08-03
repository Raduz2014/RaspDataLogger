import sys, os, bottle

sys.path = ['/home/pi/RaspDataLogger/DataloggerWebApp/html/todo/'] + sys.path
os.chdir(os.path.dirname(__file__))

import todo # This loads your application

application = bottle.app()

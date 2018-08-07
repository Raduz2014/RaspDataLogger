import sys, os, bottle

sys.path = ['/home/pi/RaspDataLogger/DataloggerWebApp/html/todo/'] + sys.path
os.chdir(os.path.dirname(__file__))
from beaker.middleware import SessionMiddleware
from bottle import Bottle
# from bottle_login import LoginPlugin

session_opts = {
    'session.type': 'file',
    'session.cookie_expires':400,
    'session.data_dir':'./sessions/',
    'session.auto': True
}

application = bottle.app()
application.config['SECRET_KEY'] = 'secret'
# login = application.install(LoginPlugin())

application = SessionMiddleware(application, session_opts)
USERS = 'admin', 'demo', 'test'

# @login.load_user
# def lod_user_by_id(user_id):
#     #load user by id
#     return USERS[user_id]

@bottle.route('/signin')
def signin():
    user_id = int(bottle.request.GET.get('user_id'))
    # login.login_user(user_id)
    return bottle.redirect('/')

@bottle.route('/tt')
def session_test():
    s = bottle.request.environ.get('beaker.session')
    s['pp']='llfffff'
    s.save()

    return bottle.redirect('/output')

@bottle.route('/output')
def output():
    s = bottle.request.environ.get('beaker.session')
    return s['pp']

import todo # This loads your application


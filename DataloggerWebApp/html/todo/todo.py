import sqlite3, os, logging
from builtUsersFile import UsersStore
import bottle
from bottle import Bottle, request, redirect
from bottle import url
from bottle import route, view, post, get, run, debug, template, static_file, error
from beaker.middleware import SessionMiddleware
application = bottle.app()


#Consts
todoDbPath = os.path.dirname(os.path.realpath(__file__)) + '/todo.db'
usersDirPath = os.path.dirname(os.path.realpath(__file__)) + '/example_conf'


# only needed when you run Bottle on mod_wsgi
bottle.debug(True)
#bottle.TEMPLATE_PATH.insert(0, "/home/pi/RaspDataLogger/DataloggerWebApp/html/todo/views")

USERS = 'admin', 'demo', 'user'

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')

@route('/login')
@view('login_form')
def login():
   
    app_session = bottle.request.environ.get('beaker.session')
    if app_session.has_key('logged_in'):
        if app_session['logged_in'] == True:
            redirect('/')
        else:
            app_session['logged_in'] = False

    return {'get_url': url}

@route('/logout')
@view('logout_form')
def logout():
    app_session = bottle.request.environ.get('beaker.session')
    if app_session.get('logged_in'):
        app_session['logged_in'] = False
        bottle.redirect('/login')
    bottle.redirect('/login')

def check_login(usrname, secret):
    storeUserFile = os.path.dirname(os.path.realpath(__file__))

    myStore = UsersStore(storeUserFile +'/usersauth.json')
    myStore.loadUsersFromFile()
    return myStore.checkUserCredential(usrname, secret)

@route('/login', method='POST')
def loginAction():
    username = request.forms.get('username')
    password = request.forms.get('password')
    app_session = bottle.request.environ.get('beaker.session')
    
    if check_login(usrname = username, secret = password):   
        app_session['logged_in'] = True
        bottle.redirect('/')
    else:
        app_session['logged_in'] = False
        bottle.redirect('/login')
    
@route('/config')
@view('config_page')
def configPage():
    app_session = bottle.request.environ.get('beaker.session')
    if app_session.has_key('logged_in'):
        if app_session['logged_in'] == False:
            redirect('/login')

    return {'get_url': url}

@route('/test2')
def testv2():
    s = bottle.request.environ.get('beaker.session')
    s['test'] = s.get('test',0)+1
    s.save()
    return 'Twast k: %d' % s['test']

@route('/')
@view('start_page')
def index():
    app_session = bottle.request.environ.get('beaker.session')
    
    if app_session.get('logged_in'):
        return {'get_url': url}
    else:
        bottle.redirect('/login')

# @route('/todo')
# def todo_list():

#     conn = sqlite3.connect(todoDbPath)
#     c = conn.cursor()
#     c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
#     result = c.fetchall()
#     c.close()

#     output = template('make_table', rows=result)
#     return output


# @route('/new', method='GET')
# def new_item():
#     if request.GET.save:

#         new = request.GET.task.strip()
#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()

#         c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
#         new_id = c.lastrowid

#         conn.commit()
#         c.close()

#         return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

#     else:
#         return template('new_task.tpl')

# @route('/edit/<no:int>', method='GET')
# def edit_item(no):

#     if request.GET.save:
#         edit = request.GET.task.strip()
#         status = request.GET.status.strip()

#         if status == 'open':
#             status = 1
#         else:
#             status = 0

#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()
#         c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
#         conn.commit()

#         return '<p>The item number %s was successfully updated</p>' % no
#     else:
#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()
#         c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
#         cur_data = c.fetchone()

#         return template('edit_task', old=cur_data, no=no)


# @route('/item<item:re:[0-9]+>')
# def show_item(item):

#         conn = sqlite3.connect('todo.db')
#         c = conn.cursor()
#         c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
#         result = c.fetchall()
#         c.close()

#         if not result:
#             return 'This item number does not exist!'
#         else:
#             return 'Task: %s' % result[0]


@route('/help')
def help():
    return static_file('help.html', root='/home/pi/RaspDataLogger/DataloggerWebApp/html/todo')


# @route('/json<json:re:[0-9]+>')
# def show_json(json):

#     conn = sqlite3.connect('todo.db')
#     c = conn.cursor()
#     c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
#     result = c.fetchall()
#     c.close()

#     if not result:
#         return {'task': 'This item number does not exist!'}
#     else:
#         return {'task': result[0]}


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


if __name__ == "__main__":
    bottle.debug(True)
    #run(reloader=True)
    bottle.run(app=app)
else:
     pass
    #  app = bottle.default_app()
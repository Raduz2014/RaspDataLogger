import sqlite3, bottle, os, logging
from bottle import route, view, post, get, run, debug, template, static_file, error
from bottle import Bottle, request, redirect
from bottle_login import LoginPlugin

#Consts
todoDbPath = os.path.dirname(os.path.realpath(__file__)) + '/todo.db'
usersDirPath = os.path.dirname(os.path.realpath(__file__)) + '/example_conf'

# only needed when you run Bottle on mod_wsgi
#from bottle import default_app
# application = bottle.default_app() 
bottle.debug(True)
#bottle.TEMPLATE_PATH.insert(0, "/home/pi/RaspDataLogger/DataloggerWebApp/html/todo/views")
app = Bottle()
app.config['SECRET_KEY'] = 'secret'

login = app.install(LoginPlugin())

#login.create_session()

USERS = 'admin', 'demo', 'user'
@login.load_user
def load_user_by_id(user_id):
    return USERS[user_id]
    #pass #load user by id here

@app.route('/')
def index():
    current_user = login.get_user()
    return current_user

@route('/test')
def test():    
    return "test page"

@app.route('/signout')
def signout():
    login.logout_user()
    return redirect('/')


@app.route('/signin')
def signin():
    user_id = int(request.GET.get('user_id'))
    login.login_user(user_id)
    return redirect('/')


@app.route('/login')
def login():
    return "login page"

@app.route('/todo')
def todo_list():

    conn = sqlite3.connect(todoDbPath)
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()

    output = template('make_table', rows=result)
    return output


@route('/new', method='GET')
def new_item():
    if request.GET.save:

        new = request.GET.task.strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,status) VALUES (?,?)", (new, 1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

    else:
        return template('new_task.tpl')

@route('/edit/<no:int>', method='GET')
def edit_item(no):

    if request.GET.save:
        edit = request.GET.task.strip()
        status = request.GET.status.strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?, status = ? WHERE id LIKE ?", (edit, status, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (str(no)))
        cur_data = c.fetchone()

        return template('edit_task', old=cur_data, no=no)


@route('/item<item:re:[0-9]+>')
def show_item(item):

        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (item,))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'Task: %s' % result[0]


@route('/help')
def help():

    return static_file('help.html', root='/home/pi/RaspDataLogger/DataloggerWebApp/html/todo')


@route('/json<json:re:[0-9]+>')
def show_json(json):

    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json,))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task': 'This item number does not exist!'}
    else:
        return {'task': result[0]}


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
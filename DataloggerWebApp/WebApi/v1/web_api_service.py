#!/usr/bin/python
from bottle import route, template

@route('/show/:item')
def show(item, db):
    row = db.execute('SELECT NameVersion from AppVersion where AppVersion=?', item).fetchone()
    if row:
        return  template('Hello {{page}}!', page=row)
    return HTTPError(404, "Page not found")

@route('/hello')
@route('/hello/<name>')
def hello(name='World'):
    return template('hello_template', name=name)

@route('/hellov2/<name>')
def index(name):
        return template('<b>Hello {{name}}</b>', name=name)

#run(host='localhost', port=8080)

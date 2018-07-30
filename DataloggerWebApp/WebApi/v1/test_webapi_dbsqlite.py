#!/usr/bin/python

import sqlite3, bottle
from bottle import route, template

application = bottle.default_app()

from bottle.ext import sqlite

#pluginSqlite = sqlite.Plugin(dbfile='/home/pi/RaspDataLogger/appdb/todo.db')
#application.install(pluginSqlite)

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    #return str(result)
    return output

#@application.route('/show/:status')
#def todov2_list(status, db):
#    rows = db.execute('SELECT id, task from todo where status=?', status).fetchall()
#    if rows:
#        return  template('make_table', rows=rows)
#    return HTTPError(404, "Page not found")



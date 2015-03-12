__author__ = 'nikitasmall'

import sqlite3
from bottle import route, run, debug, template, static_file, view

@route('/js/:filename')
def js_static(filename):
    return static_file(filename, root='./views/js')

@route('/img/:filename')
def img_static(filename):
    return static_file(filename, root='./views/img')

@route('/css/:filename')
def css_static(filename):
    return static_file(filename, root='./views/css')


@route('/todo')
def todo_list():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    output = template('views/todo', rows=result)
    return output

debug(True)
run(reloader=True)

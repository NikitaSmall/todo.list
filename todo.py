from sqlite3 import sqlite_version

__author__ = 'nikitasmall'

import sqlite3
from bottle import route, run, debug, template, static_file, view, request


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


@route('/new', method='GET')
def new_item():
    if request.GET.get('task', '').strip():
        new = request.GET.get('task', '').strip()

        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        query = "INSERT INTO todo (task, status) VALUES ('%s', 1)" %new
        c.execute(query)
        conn.commit()

        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        c.close()

        return '<p>New task approaching! %s</p>' %new_id
    else:
        return template('new_task.tpl')


debug(True)
run(reloader=True)

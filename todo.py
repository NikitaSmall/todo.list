from sqlite3 import sqlite_version

__author__ = 'nikitasmall'

import sqlite3
from bottle import route, run, debug, template, static_file, view, request, redirect, error


@route('/js/:filename')
def js_static(filename):
    return static_file(filename, root='./views/js')


@route('/img/:filename')
def img_static(filename):
    return static_file(filename, root='./views/img')

@route('/fonts/:filename')
def img_static(filename):
    return static_file(filename, root='./views/fonts')


@route('/css/:filename')
def css_static(filename):
    return static_file(filename, root='./views/css')


@route('/todo')
@route('/todo/<message>')
def todo_list(message=''):
    # message = request.GET.get('message', '').strip()

    conn = sqlite3.connect("todo.db")
    c = conn.cursor()

    c.execute("SELECT id, task, status FROM todo ORDER BY status DESC")
    result = c.fetchall()
    c.close()

    output = template('views/todo', rows=result, message=message)
    return output


@route('/new', method='GET')
@route('/new', method='POST')
def new_item():
    if request.POST.get('task', '').strip():
        new = request.POST.get('task', '').strip()

        conn = sqlite3.connect("todo.db")
        c = conn.cursor()

        query = "INSERT INTO todo (task, status) VALUES ('%s', 1)" % new
        c.execute(query)
        conn.commit()

        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        c.close()

        return redirect('/todo')
    else:
        return template('new_task.tpl')


@route('/edit/<no>', method='GET')
@route('/edit/<no>', method='POST')
def edit_item(no):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()

    if request.POST.get('save', '').strip():
        edit = request.POST.get('task', '').strip()
        status = request.POST.get('status', '').strip()

        # if status == 'open':
        #    status = 1
        # else:
        #    status = 0

        query = "UPDATE todo set task = '%s', status = '%s' WHERE id=%s" % (edit, status, no)
        c.execute(query)
        conn.commit()

        return redirect('/todo')
    else:
        query = "SELECT task, status FROM todo WHERE id like '%s'" % no
        c.execute(query)
        data = c.fetchone()

        return template('edit_task.tpl', data=data, no=no)

@route('/delete/:no', method='DELETE')
@route('/delete/:no', method='GET')
def delete_item(no):
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()

    query = "DELETE FROM todo WHERE id=%s" %no
    c.execute(query)
    conn.commit()

    return redirect('/todo')

@route('/checked', method='GET')
def check():
    conn = sqlite3.connect("todo.db")
    c = conn.cursor()

    id = request.GET.get('id', '').strip()
    isChecked = request.GET.get('isChecked', '').strip()

    query = "UPDATE todo SET status=%s WHERE id=%s" % (isChecked, id)
    c.execute(query)
    conn.commit()

    return str(isChecked)


@error(403)
def mistake(code):
    return 'something bad happened! go to <a href="/todo">main page</a>'

@error(404)
def mistake(code):
    return 'You missed! go to <a href="/todo">main page</a>'


debug(True)
run(reloader=True)

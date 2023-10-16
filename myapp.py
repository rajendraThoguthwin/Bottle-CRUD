from bottle import Bottle, run, template, request, redirect
import sqlite3

app = Bottle()


conn = sqlite3.connect('bottle.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_name TEXT NOT NULL
    )
''')
conn.commit()


@app.route('/task', method='GET')
def create_form():
    return template('create_task')

@app.route('/create', method='POST')
def create_task():
    task_name = request.forms.get('task_name')
    cursor.execute('INSERT INTO tasks (task_name) VALUES (?)', (task_name,))
    conn.commit()
    redirect('/')


@app.route('/')
def index():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return template('index', tasks=tasks)


@app.route('/edit/<task_id>', method='GET')
def edit_form(task_id):
    cursor.execute('SELECT * FROM tasks WHERE id=?', (task_id,))
    task = cursor.fetchone()
    return template('edit_task', task=task)

@app.route('/edit/<task_id>', method='POST')
def edit_task(task_id):
    new_task_name = request.forms.get('task_name')
    cursor.execute('UPDATE tasks SET task_name=? WHERE id=?', (new_task_name, task_id))
    conn.commit()
    redirect('/')


@app.route('/delete/<task_id>')
def delete_task(task_id):
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()
    redirect('/')

if __name__ == '__main__':
    run(app, debug=True)

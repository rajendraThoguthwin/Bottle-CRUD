from bottle import Bottle, request, response, template
import sqlite3

app = Bottle()

# SQLite setup
conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT
    )
''')
conn.commit()

@app.route('/tasks', method='GET')
def get_tasks():
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    return {'tasks': tasks}

@app.route('/tasks/<task_id>', method='GET')
def get_task(task_id):
    cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
    task = cursor.fetchone()
    return {'task': task}

@app.route('/tasks', method='POST')
def create_task():
    title = request.json.get('title')
    description = request.json.get('description')

    cursor.execute('INSERT INTO tasks (title, description) VALUES (?, ?)', (title, description))
    conn.commit()

    response.status = 201
    return {'message': 'Task created successfully'}

@app.route('/tasks/<task_id>', method='PUT')
def update_task(task_id):
    title = request.json.get('title')
    description = request.json.get('description')

    cursor.execute('UPDATE tasks SET title=?, description=? WHERE id=?', (title, description, task_id))
    conn.commit()

    return {'message': 'Task updated successfully'}

@app.route('/tasks/<task_id>', method='DELETE')
def delete_task(task_id):
    cursor.execute('DELETE FROM tasks WHERE id=?', (task_id,))
    conn.commit()

    return {'message': 'Task deleted successfully'}

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)

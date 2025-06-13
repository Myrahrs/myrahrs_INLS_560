from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

DB_NAME = 'tasks.db'

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')) NOT NULL DEFAULT 'Medium',
            completed INTEGER NOT NULL DEFAULT 0
        )
        ''')
    print("Database initialized.")

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def get_tasks(priority=None, show_completed=None):
    conn = get_db_connection()
    query = "SELECT * FROM tasks"
    filters = []
    params = []

    if priority and priority != 'All':
        filters.append("priority = ?")
        params.append(priority)
    
    if show_completed is not None:
        filters.append("completed = ?")
        params.append(1 if show_completed else 0)
    
    if filters:
        query += " WHERE " + " AND ".join(filters)

    query += " ORDER BY due_date IS NULL, due_date ASC"  # Tasks with no due date go last

    tasks = conn.execute(query, params).fetchall()
    conn.close()
    return tasks

def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return task

def add_task(title, description, due_date, priority):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (title, description, due_date, priority) VALUES (?, ?, ?, ?)",
        (title, description, due_date, priority)
    )
    conn.commit()
    conn.close()

def update_task(task_id, title, description, due_date, priority, completed):
    conn = get_db_connection()
    conn.execute('''
        UPDATE tasks SET title=?, description=?, due_date=?, priority=?, completed=?
        WHERE id=?
    ''', (title, description, due_date, priority, completed, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

@app.route('/')
def index():
    priority_filter = request.args.get('priority', 'All')
    show_completed = request.args.get('show_completed', 'false').lower() == 'true'
    tasks = get_tasks(priority=priority_filter, show_completed=show_completed)
    return render_template('index.html', tasks=tasks, selected_priority=priority_filter, show_completed=show_completed)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        due_date = request.form.get('due_date', None)
        priority = request.form.get('priority', 'Medium')
        add_task(title, description, due_date, priority)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = get_task(task_id)
    if not task:
        return "Task not found", 404

    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        due_date = request.form.get('due_date', None)
        priority = request.form.get('priority', 'Medium')
        completed = 1 if request.form.get('completed') == 'on' else 0
        update_task(task_id, title, description, due_date, priority, completed)
        return redirect(url_for('index'))

    return render_template('edit_task.html', task=task)

@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

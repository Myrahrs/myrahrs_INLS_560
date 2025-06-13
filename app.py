# Python App for creating a Flask/SQLite Task list in HTML and CSS

# Import necessary modules from Flask and SQLite
from flask import Flask, render_template, request, redirect, url_for
import sqlite3  # To interact with the SQLite database

# Initialize the Flask app
app = Flask(__name__)

# -----------------------------------------------
# Function to initialize the database
# This will create the 'tasks' table if it doesn't already exist
def init_db():
    with sqlite3.connect('tasks.db') as conn:
        # Create the 'tasks' table if it doesn't already exist
        # Fields: id (auto-incrementing primary key), title (required), description (optional)
        conn.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT
        )
        ''')
    print("Database initialized.")  # Confirmation message for developer

# -----------------------------------------------
# Function to populate sample tasks (only if the table is empty)
def populate_sample_tasks():
    sample_tasks = [
        ("Buy groceries", "Milk, eggs, bread, and spinach"),
        ("Study for INLS 560", "Review Flask and SQLite lessons"),
        ("Call the vet", "Schedule check-up for Luna the cat"),
        ("Finish project", "Push final version to GitHub and update README"),
        ("Clean desk", "Tidy workspace before the weekend")
    ]

    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM tasks')  # Check how many tasks exist
        count = cursor.fetchone()[0]

        # Only insert sample tasks if table is empty
        if count == 0:
            cursor.executemany(
                'INSERT INTO tasks (title, description) VALUES (?, ?)',
                sample_tasks
            )
            print("Sample tasks inserted.")
        else:
            print("Tasks already exist — skipping sample data.")

# -----------------------------------------------
# Function to fetch all tasks from the database
def get_tasks():
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()  # Create a cursor to interact with DB
        cursor.execute('SELECT * FROM tasks')  # Fetch all task records
        tasks = cursor.fetchall()  # Store results as a list of tuples
    return tasks

# -----------------------------------------------
# Function to add a new task to the database
def add_task(title, description):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute(
            'INSERT INTO tasks (title, description) VALUES (?, ?)',
            (title, description)  # Use parameterized queries for security
        )

# -----------------------------------------------
# Function to delete a task based on its ID
def delete_task(task_id):
    with sqlite3.connect('tasks.db') as conn:
        conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))

# -----------------------------------------------
# Route for the homepage ("/")
# Displays all current tasks
@app.route('/')
def index():
    tasks = get_tasks()  # Retrieve all tasks from the database
    return render_template('index.html', tasks=tasks)  # Render the home page with task data

# -----------------------------------------------
# Route for adding a new task ("/add")
# Supports both GET and POST methods
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Get data entered by the user in the form
        title = request.form['title']
        description = request.form['description']
        add_task(title, description)  # Save the new task to the database
        return redirect(url_for('index'))  # Redirect to the homepage
    return render_template('add_task.html')  # Show the add task form (GET request)

# -----------------------------------------------
# Route for deleting a task ("/delete/<task_id>")
@app.route('/delete/<int:task_id>')
def delete(task_id):
    delete_task(task_id)  # Delete the task with the given ID
    return redirect(url_for('index'))  # Refresh the homepage to reflect deletion

# -----------------------------------------------
# Run the app only if this script is executed directly
if __name__ == '__main__':
    init_db()             # Ensure the database and table exist
    populate_sample_tasks()  # Insert sample data if none exists
    app.run(debug=True)   # Start the development server with debug mode on

# Flask Task List Application

## Overview

This is a simple web application built with **Flask** and **SQLite** that allows users to manage a task list through a web browser. Users can:

- View all tasks
- Add new tasks with a title and optional description
- Delete existing tasks

The app uses a SQLite database (`tasks.db`) to store task data persistently.

---

## Project Structure

```
assignment_09/
└── SQL_Flask/
    ├── static/
    │   └── style.css          # CSS styling for the web pages
    ├── templates/
    │   ├── add_task.html      # HTML form template to add new tasks
    │   └── index.html         # HTML template to display all tasks
    ├── app.py                 # Main Flask application script
    ├── README.md              # This project documentation file
    └── tasks.db               # SQLite database (auto-generated on first run)
```

---

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system
- `pip` package manager
- Recommended: Create and activate a Python virtual environment

### Install Dependencies

Open your terminal/command prompt and run:

```bash
pip install Flask
```

---

## Features

- **Homepage (/)**: View all current tasks
- **Add Task (/add)**: Add a new task via a form
- **Delete Task (/delete/<task_id>)**: Delete a task by clicking the delete link
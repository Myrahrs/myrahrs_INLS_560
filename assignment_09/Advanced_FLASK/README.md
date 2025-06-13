# Advanced Flask Task List Application

## Overview

This is an enhanced version of the basic Flask/SQLite task list app. It demonstrates:

- Tasks with due dates and priority levels (Low, Medium, High)
- Ability to mark tasks as completed
- Edit existing tasks
- Filter tasks by priority and completion status
- Sort tasks by due date
- Bootstrap integration for clean UI

---

## Project Structure

```
assignment_09/
└── Advanced_FLASK/
    ├── static/
    │   └── style.css          # Optional custom CSS
    ├── templates/
    │   ├── add_task.html      # Add task form
    │   ├── edit_task.html     # Edit task form
    │   └── index.html         # Homepage task list
    ├── app.py                 # Main Flask app
    ├── README.md              # This file
    └── tasks.db               # SQLite database (auto-created)
```

---

## Setup Instructions

### Prerequisites

- Python 3.x installed
- pip package manager
- (Recommended) Create and activate a virtual environment

### Install Dependencies

```bash
pip install Flask
```

### Running the App

1. Run the app:

```bash
python app.py
```

2. Open your browser to http://127.0.0.1:5000

---

## Usage

- **View tasks** on the homepage, filter by priority or show/hide completed tasks
- **Add tasks** with title, optional description, due date, and priority
- **Edit existing tasks**, update their details or mark as completed
- **Delete tasks** when no longer needed
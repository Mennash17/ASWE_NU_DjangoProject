# ASWE_NU_DjangoProject
ASWE_NU_2025SPR_Project1

Simply Todo
Project Overview

Simply Todo is a simple task management application built with Django. It allows users to create, update, and delete tasks. The application is styled using plain CSS.

## Features
- **Create Tasks**: Users can add new tasks with a title, description, and completion status.
- **Update Tasks**: Users can edit existing tasks.
- **Delete Tasks**: Users can remove tasks from the list.
- **Task List**: Displays all tasks with their details.

## Installation
### Prerequisites

- Python 3.x
- Django 5.x

### Steps

1. Clone the Repository:
   ```bash
   git clone <repository-url>
   cd simply_todo
   ```

2. Create a Virtual Environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install Dependencies:
   ```bash
   pip install django
   ```

4. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

### Creating a Task

1. Fill out the form with the task title, description, and completion status.
2. Click the "Add Task" button.

### Updating a Task

1. Click the "Edit" button next to the task you want to update.
2. Modify the task details in the form.
3. Click the "Update Task" button.

### Deleting a Task

1. Click the "Delete" button next to the task you want to remove.
2. Confirm the deletion.

## Project Structure

```
simply_todo/
├── simply_todo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── tasks/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_update.html
│   │       ├── task_delete.html
│   ├── static/
│   │   └── tasks/
│   │       └── styles.css
├── staticfiles/
├── manage.py
```

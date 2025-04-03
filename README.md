# Simply Todo

## Project Overview
Simply Todo is a simple task management application built with Django. It allows users to create, update, delete, and export tasks. The application is styled using plain CSS and is published online on Render at [https://simply-todo.onrender.com](https://simply-todo.onrender.com).

## Features

### Phase 1:
- **Create Tasks**: Users can add new tasks with a title, description, and completion status.
- **Update Tasks**: Users can edit existing tasks.
- **Delete Tasks**: Users can remove tasks from the list.
- **Task List**: Displays all tasks with their details.

### Phase 2:
Implemented advanced features enhancing user experience and functionality:

1. **User Authentication**:
   - Users can register, log in, and manage their own tasks securely.
   - Password reset functionality.

2. **Task Categories**:
   - Tasks can be categorized (e.g., Work, Personal, Urgent).
   - Filtering tasks by category.

3. **Due Dates and Reminders**:
   - Users can set due dates for tasks.
   - Reminder notifications for upcoming deadlines.

4. **Priority Levels**:
   - Tasks can be assigned priority levels (High, Medium, Low).
   - Sorting tasks based on priority.

5. **Search Functionality**:
   - Quickly find tasks by title or description.

6. **Task Comments**:
   - Users can add notes or comments for additional context.

7. **Task Completion Progress**:
   - Visual indicators for task progress (percentage complete).

8. **Export Tasks (New)**:
   - Export tasks functionality using a REST API endpoint.
   - JavaScript frontend integration for seamless exporting to Excel or PDF formats.

## Installation

### Prerequisites
- Python 3.x
- Django 5.x

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Mennash17/ASWE_NU_DjangoProject
   cd ASWE_NU_DjangoProject
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install django djangorestframework pandas openpyxl
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
   - Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your web browser.

## Usage

### Creating a Task
1. Fill out the form with the task title, description, and completion status.
2. Click "Add Task."

### Updating a Task
1. Click "Edit" next to the task you want to update.
2. Modify details and click "Update Task."

### Deleting a Task
1. Click "Delete" next to the task you want to remove.
2. Confirm deletion.

### Exporting Tasks (New)
1. Click "Export Tasks" on the frontend.
2. Select desired export format (Excel or PDF).
3. Confirm export to download your tasks.

## Project Structure
```
ASWE_NU_DjangoProject/
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
│   ├── serializers.py (new)
│   ├── templates/
│   │   └── tasks/
│   │       ├── task_list.html
│   │       ├── task_update.html
│   │       ├── task_delete.html
│   ├── static/
│   │   └── tasks/
│   │       ├── styles.css
│   │       ├── export.js (new)
├── staticfiles/
├── manage.py
```

## Deployment
The application is deployed and publicly accessible on Render:
- [Simply Todo](https://simply-todo.onrender.com)

---

*ASWE_NU_2025SPR_Project1*


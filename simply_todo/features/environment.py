import os
import django
import sys

def before_all(context):
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    print(">>> Django Settings Loaded:", os.environ.get('DJANGO_SETTINGS_MODULE'))
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simply_todo.simply_todo.settings')
    
    django.setup()
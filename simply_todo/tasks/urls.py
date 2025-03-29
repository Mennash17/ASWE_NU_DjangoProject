from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import TaskListCreateAPIView
from .views import export_tasks_excel_api

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('update/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/<int:pk>/json/', views.task_detail_json, name='task_detail_json'),
    path('register/', views.register, name='register'),
    
    # Use Django's built-in LoginView for login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    
    # Logout will redirect to the login page
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # API routes
    path('api/tasks/', views.task_list_api, name='task_list_api'),
    path('api/tasks/', TaskListCreateAPIView.as_view(), name='task-list-create'),
    path('api/export/excel/', export_tasks_excel_api, name='export_tasks_excel_api')
]

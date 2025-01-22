from django.urls import path

from . import views
app_name = 'task_manager'
urlpatterns = [
    path('task-manager/', views.task_manager_view, name='task_manager'),
    path('', views.task, name='task'),
]

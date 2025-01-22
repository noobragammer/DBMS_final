from django.urls import path
from . import views

urlpatterns = [
    path('task-manager/', views.task_manager_view, name='task_manager'),
    path('', views.task, name='task'),
]

from django.urls import path
from . import views

app_name = 'task_manager'

urlpatterns = [
    path('', views.task_manager_view, name='task_manager'),
    path('add-task/', views.add_task, name='add_task'),
    path('edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    path('delete-task/<int:pk>/', views.delete_task, name='delete_task'),
     path('update-status/<int:pk>/', views.update_task_status, name='update_task_status'),
]

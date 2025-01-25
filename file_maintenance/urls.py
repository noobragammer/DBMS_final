from django.urls import path
from . import views

app_name = 'file_maintenance'

urlpatterns = [
    path('user-maintenance/', views.user_maintenance_view, name='user_maintenance'),
    path('equipment-maintenance/', views.equipment_maintenance_view, name='equipment_maintenance'),
    path('add-equipment/', views.add_equipment, name='add_equipment'),
    path('edit-equipment/<int:equipment_id>/', views.edit_equipment, name='edit_equipment'),
    path('delete-equipment/<int:equipment_id>/', views.delete_equipment, name='delete_equipment'),
    path('add-user/', views.add_user, name='add_user'),
]

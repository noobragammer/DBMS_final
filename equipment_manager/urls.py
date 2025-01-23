from django.urls import path
from . import views

app_name = 'equipment_manager'

urlpatterns = [
    path('manage-equipment/', views.manage_equipment, name='manage_equipment'),
    path('', views.equipment, name='equipment'),  # Added route for equipment.html
]

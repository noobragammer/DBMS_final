from django.urls import path
from . import views

app_name = 'equipment_manager'

urlpatterns = [
    path('', views.manage_equipment, name='equipment'),  # Added route for equipment.html
]

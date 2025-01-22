from django.urls import path
from . import views

urlpatterns = [
    path('manage-equipment/', views.manage_equipment, name='manage_equipment'),
    path('', views.equipment, name='equipment'),  # Added route for equipment.html
]

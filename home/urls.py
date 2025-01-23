from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('events/', views.get_events, name='get_events'),
]


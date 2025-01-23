from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_view'),
    path('events/', views.get_events, name='get_events'),
]


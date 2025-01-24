from django.urls import path
from . import views

app_name = 'inbox'  # Replace with your app name if needed

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
]
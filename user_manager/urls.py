from django.urls import path
from . import views

app_name = 'user_manager'

urlpatterns = [
    path('users/', views.manage_users_view, name='manage_users'),
    path('', views.user, name='user'),
]

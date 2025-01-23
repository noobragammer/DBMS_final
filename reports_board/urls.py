from django.urls import path

from . import views

app_name = 'reports_board'

urlpatterns = [
    path('reports/', views.report_view, name='report_view'),
    path('', views.report, name='report'),
]


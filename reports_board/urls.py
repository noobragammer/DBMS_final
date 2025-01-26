from django.urls import path
from . import views

app_name = 'reports_board'

urlpatterns = [
    path('', views.report, name='report'),
    path('generate-pie-chart/', views.generate_pie_chart, name='generate_pie_chart'),
]


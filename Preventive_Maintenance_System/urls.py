"""
URL configuration for Preventive_Maintenance_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('login/', permanent=False)), 
    path('admin/', admin.site.urls),
    path('file_maintenance/', include('file_maintenance.urls')),
    path('equipment_manager/', include('equipment_manager.urls')),
    path('task_manager/', include('task_manager.urls')),
    path('reports_board/', include('reports_board.urls')),
    path('login/', include('login.urls')),
    path('inbox/', include('inbox.urls')),
    path('home/', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

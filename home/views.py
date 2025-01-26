from django.shortcuts import render
from django.http import JsonResponse
from file_maintenance.models import Equipment
from task_manager.models import Task
from login.models import User
from django.db.models import Q





def dashboard(request):
    finished_tasks_count = Task.objects.filter(status='Completed').count()  # Adjust filter as needed
    equipment_count = Equipment.objects.count()
    users_count = User.objects.count()
    upcoming_tasks_count = Task.objects.filter(Q(status='Pending') | Q(status='Approved')).count()
    
    context = {
        'finished_tasks_count': finished_tasks_count,
        'equipment_count': equipment_count,
        'users_count': users_count,
        'upcoming_tasks_count': upcoming_tasks_count,
    }
    
    return render(request, 'home/dashboard.html', context)
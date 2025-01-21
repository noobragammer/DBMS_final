from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse


def get_events(request):
    events = [
        {"title": "Meeting", "start": "2023-01-25", "end": "2023-01-26"},
        {"title": "Task Due", "start": "2023-01-28"},
    ]
    return JsonResponse(events, safe=False)

def dashboard_view(request):
    return render(request, 'home/dashboard.html')
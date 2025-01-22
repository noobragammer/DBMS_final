from django.shortcuts import redirect
from django.urls import resolve

class RoleBasedAccessMiddleware:
    APP_ACCESS = {
        'equipment_manager': ['Technician', 'Admin'],
        'file_maintenance': ['Admin'],
        'home': ['Employee', 'Technician', 'Admin'],
        'inbox': ['Employee', 'Technician', 'Admin'],
        'reports_board': ['Technician', 'Admin'],
        'task_manager': ['Employee', 'Technician', 'Admin'],
    }

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            app_name = resolve(request.path).app_name  # Get the app name from the URL
            if app_name in self.APP_ACCESS:
                allowed_roles = self.APP_ACCESS[app_name]
                if request.user.role not in allowed_roles:
                    return redirect('home:dashboard')  # Redirect unauthorized users to the dashboard
        return self.get_response(request)
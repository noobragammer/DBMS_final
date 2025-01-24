from django.shortcuts import render

def manage_users_view(request):
    # Example data for the user management table
    users = [
        {
            'ID': '1',
            'name': 'Gibe Bartelome',
            'role': 'Admin',
            'permissions': {
                'equipment': True,
                'task_manager': True,
                'reports': True,
                'user_manager': True,
                'file_maintenance': True
            }
        },
        {
            'ID': '2',
            'name': 'Xyron Newell Y. Relon',
            'role': 'User',
            'permissions': {
                'equipment': True,
                'task_manager': True,
                'reports': False,
                'user_manager': False,
                'file_maintenance': True
            }
        },
        {
            'ID': '3',
            'name': 'Jaffy Myll Fuentes',
            'role': 'Technician',
            'permissions': {
                'equipment': False,
                'task_manager': True,
                'reports': False,
                'user_manager': False,
                'file_maintenance': False
            }
        },
        {
            'ID': '4',
            'name': 'Shane Agbon',
            'role': 'Technician',
            'permissions': {
                'equipment': False,
                'task_manager': True,
                'reports': False,
                'user_manager': False,
                'file_maintenance': False
            }
        }
    ]

    return render(request, 'user_manager/user.html', {'users': users})

def user(request):
    return render(request, "user_manager/user.html")

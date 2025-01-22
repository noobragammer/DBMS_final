from django.shortcuts import render

def task_manager_view(request):
    # Example data to display in the Task Manager table
    tasks = [
        {
            'serial_no': 'IT01',
            'name': 'Xyron Newell Y. Relon',
            'equipment': 'Keyboard',
            'category': 'Hardware',
            'request_form': 'request.pdf',
            'technician': 'Jaffy Myll Fuentes',
            'priority': 'Low',
            'status': 'Approved'
        }
    ]

    return render(request, 'task_manager/task.html', {'tasks': tasks})

def task(request):
    return render(request, "task_manager/task.html")

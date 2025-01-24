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

def add_task(request):
    """
    Handle the Add Task page and form submission.
    """
    if request.method == 'POST':
        # Retrieve form data
        # owner = request.POST.get('owner')
        # category = request.POST.get('category')
        # technician = request.POST.get('technician')
        # priority = request.POST.get('priority')
        # comment = request.POST.get('comment')

        # # Save the task to the database (if you have a model set up)
        # # Example: Task.objects.create(owner=owner, category=category, technician=technician, priority=priority, comment=comment)

        # # Redirect back to the task manager page or another page after saving
        # return redirect('task_manager:task_manager')
        pass
    return render(request, 'task_manager/add_task.html')

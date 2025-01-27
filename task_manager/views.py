from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .forms import TaskForm
from .models import Task
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now

def task_manager_view(request):
    tasks = Task.objects.filter(status__in=['Pending', 'Approved'])
    return render(request, 'task_manager/task.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_manager:task_manager')
        else:
            messages.error(request, 'There was an error creating the task.')
    else:
        form = TaskForm()

    return render(request, 'task_manager/add_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        # Update task fields with form data
        task.equipment_name = request.POST.get("equipment_name")
        task.equipment_category = request.POST.get("equipment_category")
        task.technician_name = request.POST.get("technician_name", "")  # Optional field
        task.priority = request.POST.get("priority")
        task.status = request.POST.get("status")

        # Save the task to the database
        task.save()

        # Add a success message
        messages.success(request, "Task updated successfully!")

        # Redirect to the Task Manager view
        return redirect("task_manager:task_manager")

    # Render the edit form with the current task data
    context = {
        "task": task
    }
    return render(request, "task_manager/edit_task.html", context)

def delete_task(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_manager:task_manager')
    else:
        messages.error(request, 'Task deleted unsuccessful!')
        return redirect('task_manager:task_manager')

@csrf_exempt
def update_task_status(request, pk):
    task = get_object_or_404(Task, id=pk)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status in dict(Task._meta.get_field("status").choices):  # Validate status
            if new_status == "Completed" and task.status != "Completed":
                task.date_completed = now()
            task.status = new_status
            task.save()
            messages.success(request, "Task status updated successfully!")
            return redirect('task_manager:task_manager')
        else:
            return JsonResponse({"success": False, "message": "Invalid status"})
    
    return JsonResponse({"success": False, "message": "Invalid request"})
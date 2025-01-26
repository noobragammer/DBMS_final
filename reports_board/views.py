from django.http import HttpResponse
from task_manager.models import Task
from django.shortcuts import render
from io import BytesIO
import matplotlib.pyplot as plt
from django.urls import reverse
from django.utils.timezone import now, timedelta
from datetime import datetime

def generate_pie_chart(request):
    statuses = Task.objects.values_list('status', flat=True)
    status_counts = {
        "Pending": statuses.filter(status="Pending").count(),
        "Approved": statuses.filter(status="Approved").count(),
        "Completed": statuses.filter(status="Completed").count(),
    }

    # Create a pie chart
    labels = status_counts.keys()
    sizes = status_counts.values()
    colors = ['yellow', 'blue', 'green']
    explode = (0.1, 0, 0)  # Highlight the first slice

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    # Save the plot to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(buffer, content_type='image/png')


def report(request):
    chart_url = reverse('reports_board:generate_pie_chart')
    return render(request, 'reports_board/report.html', {'chart_url': chart_url})

def generate_multiple_graphs(request):
    # Get the current date and time
    current_date = now()

    # Calculate the start of the past month
    start_date = current_date - timedelta(days=30)

    # Query for completed tasks in the past month
    completed_tasks = Task.objects.filter(status="Completed", completed_date__range=[start_date, current_date])

    # Group tasks by day
    tasks_by_day = {}
    for task in completed_tasks:
        day = task.completed_date.date()  # Extract the date part
        tasks_by_day[day] = tasks_by_day.get(day, 0) + 1

    # Prepare data for the graph
    days = sorted(tasks_by_day.keys())
    counts = [tasks_by_day[day] for day in days]

    # Generate the line chart
    plt.figure(figsize=(10, 6))
    plt.plot(days, counts, marker='o', linestyle='-', color='blue', label='Completed Tasks')
    plt.title('Completed Tasks Over the Past Month')
    plt.xlabel('Date')
    plt.ylabel('Number of Completed Tasks')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()

    # Save the chart to a BytesIO buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Return the image as an HTTP response
    return HttpResponse(buffer, content_type='image/png')
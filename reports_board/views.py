from django.http import HttpResponse
from task_manager.models import Task
from django.shortcuts import render
from io import BytesIO
import matplotlib.pyplot as plt
from django.urls import reverse
from django.utils.timezone import now, timedelta
from datetime import datetime
from task_manager.models import Task

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
    tasks = Task.objects.filter(status='Completed')
    chart_url = reverse('reports_board:generate_pie_chart')
    return render(request, 'reports_board/report.html', {'tasks':tasks,'chart_url': chart_url})

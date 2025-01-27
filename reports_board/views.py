from django.http import HttpResponse
from task_manager.models import Task
from django.shortcuts import render
from io import BytesIO
import matplotlib.pyplot as plt
from django.urls import reverse
from django.utils.timezone import now, timedelta
from datetime import datetime
from task_manager.models import Task
from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from django.templatetags.static import static
import os
from django.conf import settings
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Image,
    Spacer,
)
from reportlab.platypus import Frame

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


def generate_task_report_pdf(request):
    # Create buffer for PDF
    buffer = BytesIO()
    pdf = SimpleDocTemplate(buffer, pagesize=landscape(A4), leftMargin=50, rightMargin=50, topMargin=10, bottomMargin=50)
    elements = []

    # Add the letterhead image
    letterhead_path = os.path.join(settings.STATICFILES_DIRS[0], 'images', 'letterhead.png')
    try:
        img = Image(letterhead_path)
        img.drawHeight = 100  # Adjust image height
        img.drawWidth = 600  # Adjust image width
        elements.append(img)
    except Exception as e:
        elements.append(Paragraph(f"Error loading letterhead: {str(e)}", getSampleStyleSheet()["Normal"]))

    # Add a title
    styles = getSampleStyleSheet()
    title = Paragraph("<b>Task Report</b>", styles["Title"])
    elements.append(title)
    elements.append(Spacer(1, 20))  # Add spacing

    # Fetch task data
    tasks = Task.objects.all()

    # Prepare table data
    table_data = [["Equipment Name", "Category", "Priority", "Technician", "Status", "Created At", "Completed At", "Comment"]]  # Header row
    for task in tasks:
        table_data.append([
            task.equipment_name,
            task.equipment_category,  # Display choice value for category
            task.priority,  # Display choice value for priority
            task.technician_name if task.technician_name else "N/A",
            task.status,
            task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            task.date_completed.strftime("%Y-%m-%d %H:%M:%S") if task.date_completed else "N/A",
            task.comment if task.comment else "N/A",  # Add the comment field
        ])


    # Style the table
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  # Header background
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  # Header text color
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Center alignment
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Bold font for header
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),  # Padding for header
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  # Row background
        ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Grid lines
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  # Regular font for rows
        ('FONTSIZE', (0, 0), (-1, -1), 9),  # Smaller font for data rows
    ])
    # Add table to the PDF
    table = Table(table_data, colWidths=[80, 80, 60, 80, 60, 90, 90, 120])  # Adjust column widths as needed
    table.setStyle(table_style)
    elements.append(table)

    # Build the PDF
    pdf.build(elements)
    buffer.seek(0)

    # Return the PDF as an HTTP response
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="task_report.pdf"'
    return response


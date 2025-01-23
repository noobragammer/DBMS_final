from django.shortcuts import render

def report_view(request):
    # Example data to populate the reports table and details section
    reports = [
        {
            'serial_no': 'IT01',
            'name': 'Xyron Newell Y. Relon',
            'equipment': 'Keyboard',
            'category': 'Hardware',
            'request_form': 'request.pdf',
            'technician': 'Jaffy Myll Fuentes',
            'priority': 'Low',
            'status': 'Approved',
            'maintenance_date': '-'
        }
    ]

    # Pass the reports data to the template
    return render(request, 'reports_board/report.html', {'reports': reports})

def report(request):
    return render(request, "reports_board/report.html")
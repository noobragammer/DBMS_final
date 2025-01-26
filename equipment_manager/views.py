from django.shortcuts import render
from file_maintenance.models import Equipment

def manage_equipment(request):
    equipment = Equipment.objects.all()  # Fetch all equipment records
    return render(request, 'equipment_manager/equipment.html', {'equipment': equipment})



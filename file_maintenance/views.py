from django.shortcuts import render, redirect
from .forms import EquipmentForm
from login.models import User
from .models import Equipment
from django.contrib import messages
from django.shortcuts import get_object_or_404

users = User.objects.all()

def user_maintenance_view(request):
    # Example data for user maintenance
    return render(request, 'file_maintenance/user_maintenance.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        # Handle the form submission logic here (if needed)
        # For now, simply render the page without processing
        pass
    return render(request, 'file_maintenance/add_user.html')

def equipment_maintenance_view(request):
    equipments = Equipment.objects.all()
    return render(request, 'file_maintenance/equip_maintenance.html', {'equipments': equipments})


def add_equipment(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        print("POST Data:", request.POST)
        if form.is_valid():
            print("Saving equipment...")
            form.save()
            messages.success(request, "Equipment added successfully!")
            return redirect('file_maintenance:equipment_maintenance')
        else:
            print("Form errors:", form.errors)
            messages.error(request, "Failed to add equipment. Please check the form for errors.")
    else:
        form = EquipmentForm()
        print("Rendering form")
    return render(request, 'file_maintenance/add_equipment.html', {'form': form})

def edit_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)

    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipment updated successfully!")
            return redirect('file_maintenance:equipment_maintenance')
        else:
            messages.error(request, "Failed to update equipment. Please check the form for errors.")
    else:
        form = EquipmentForm(instance=equipment)

    return render(request, 'file_maintenance/edit_equipment.html', {'form': form, 'equipment': equipment})

def delete_equipment(request, equipment_id):
    equipment = get_object_or_404(Equipment, id=equipment_id)

    if request.method == 'POST':
        equipment.delete()
        messages.success(request, "Equipment deleted successfully!")
        return redirect('file_maintenance:equipment_maintenance')

    return render(request, 'file_maintenance/confirm_delete_equipment.html', {'equipment': equipment})


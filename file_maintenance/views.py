from django.shortcuts import render, redirect
from .forms import EquipmentForm
from login.models import User
from .models import Equipment
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError



def user_maintenance_view(request):
    users = User.objects.all()
    return render(request, 'file_maintenance/user_maintenance.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        data = request.POST
        try:
            user = User(
                first_name=data['first_name'],
                last_name=data['last_name'],
                username=data['username'],
                email_address=data['email_address'],
                contact_number=data['contact_number'],
                password=data['password'],
                role=data['role'],
                signature=request.FILES.get('signature', None),
            )
            user.full_clean()
            user.save()
            messages.success(request, "User added successfully!")
            return redirect('file_maintenance:user_maintenance')
        except ValidationError as e:
            messages.error(request, f"Error: {e.message_dict}")
    return render(request, 'file_maintenance/add_user.html')

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        data = request.POST
        try:
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.username = data['username']
            user.email_address = data['email_address']
            user.contact_number = data['contact_number']
            user.role = data['role']
            if 'password' in data and data['password']:
                user.password = data['password']
            if 'signature' in request.FILES:
                user.signature = request.FILES['signature']
            user.full_clean()
            user.save()
            messages.success(request, "User updated successfully!")
            return redirect('file_maintenance:user_maintenance')
        except ValidationError as e:
            messages.error(request, f"Error: {e.message_dict}")
    return render(request, 'file_maintenance/edit_user.html', {'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully!")
        return redirect('file_maintenance:user_maintenance')
    return render(request, 'file_maintenance/user_maintenance.html', {'user': user})

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


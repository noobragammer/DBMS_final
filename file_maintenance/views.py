from django.shortcuts import render

def user_maintenance_view(request):
    # Example data for user maintenance
    users = [
        {
            'id': 1,
            'name': 'Gibe Bartolome',
            'email': 'bartolome@gmail.com',
            'contact': '09171234567',
            'role': 'Admin',
            'signature': 'signature1.png',
            'username': 'admin',
            'password': '*******'
        },
        {
            'id': 2,
            'name': 'Xyron Newell Y. Relon',
            'email': 'relon@gmail.com',
            'contact': '09181234567',
            'role': 'User',
            'signature': 'signature2.png',
            'username': 'xyron',
            'password': '*******'
        },
        {
            'id': 3,
            'name': 'Jaffy Myll Fuentes',
            'email': 'fuentes@gmail.com',
            'contact': '09191234567',
            'role': 'Technician',
            'signature': 'signature3.png',
            'username': 'jaffy',
            'password': '*******'
        },
        {
            'id': 4,
            'name': 'Shane Agbon',
            'email': 'agbon@gmail.com',
            'contact': '09161234567',
            'role': 'Technician',
            'signature': 'signature4.png',
            'username': 'shane',
            'password': '*******'
        },
    ]

    return render(request, 'file_maintenance/user_maintenance.html', {'users': users})

def add_user(request):
    if request.method == 'POST':
        # Handle the form submission logic here (if needed)
        # For now, simply render the page without processing
        pass
    return render(request, 'file_maintenance/add_user.html')

def equipment_maintenance_view(request):
    # Example data for equipment maintenance
    equipment_list = [
        {
            'id': 1,
            'name': 'Keyboard',
            'owner': 'Xyron Newell Relon',
            'category': 'Hardware',
            'frequency': 'Monthly',
            'status': 'Active'
        },
        {
            'id': 2,
            'name': 'Microsoft Office',
            'owner': 'Xyron Newell Relon',
            'category': 'Software',
            'frequency': 'Monthly',
            'status': 'Active'
        },
        {
            'id': 3,
            'name': 'Aircon',
            'owner': 'Xyron Newell Relon',
            'category': 'Utility',
            'frequency': 'Yearly',
            'status': 'Active'
        },
    ]

    return render(request, 'file_maintenance/equip_maintenance.html', {'equipment_list': equipment_list})

def add_equipment(request):
    """Renders the Equipment Maintenance page."""
    if request.method == 'POST':
        name = request.POST.get('name')
        owner = request.POST.get('owner')
        category = request.POST.get('category')
        frequency = request.POST.get('frequency')
        status = request.POST.get('status')
        # You can add logic to handle this data or display a success message.
        print(f"Equipment added: {name}, {owner}, {category}, {frequency}, {status}")

    return render(request, 'file_maintenance/add_equip.html')



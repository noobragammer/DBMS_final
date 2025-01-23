from django.shortcuts import render

def manage_equipment(request):
    # Example data to populate the table; replace with database queries if needed
    equipment_list = [
        {"serial_no": "IT01", "name": "Keyboard", "category": "Hardware", "date": 2024, "frequency": "Monthly", "status": "Active"},
        {"serial_no": "IT01", "name": "Microsoft Office", "category": "Software", "date": 2024, "frequency": "Monthly", "status": "Active"},
        {"serial_no": "IT00", "name": "Aircon", "category": "Utility", "date": 2012, "frequency": "Yearly", "status": "Active"},
    ]

    context = {
        "equipment_list": equipment_list
    }

    return render(request, "equipment_manager/equipment.html", context)

def equipment(request):
    return render(request, "equipment_manager/equipment.html")  # New view for equipment.html

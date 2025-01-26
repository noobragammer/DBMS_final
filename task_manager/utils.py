from datetime import date, timedelta
from file_maintenance.models import Equipment
from task_manager.models import Task

def create_maintenance_tasks():
    """Generate tasks for equipment nearing maintenance dates."""
    today = date.today()
    start_date = today + timedelta(days=3)
    end_date = today + timedelta(days=4)

    equipment_list = Equipment.objects.filter(status=Equipment.ACTIVE)

    for equipment in equipment_list:
        next_date = equipment.next_maintenance_date()
        if next_date and start_date <= next_date <= end_date:
            # Avoid duplicate tasks
            if not Task.objects.filter(
                equipment_name=equipment.name,
                equipment_category=equipment.category,
                status='Pending',
            ).exists():
                Task.objects.create(
                    equipment_name=equipment.name,
                    equipment_category=equipment.category,
                    priority='medium',  # Default priority, can be customized
                    comment=f"Scheduled maintenance for {equipment.name} on {next_date}.",
                )

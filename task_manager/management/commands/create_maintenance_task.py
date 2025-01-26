from django.core.management.base import BaseCommand
from task_manager.utils import create_maintenance_tasks

class Command(BaseCommand):
    help = "Generate tasks for equipment nearing maintenance dates"

    def handle(self, *args, **kwargs):
        create_maintenance_tasks()
        self.stdout.write(self.style.SUCCESS("Maintenance tasks generated successfully!"))

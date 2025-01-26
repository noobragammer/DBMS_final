from celery import shared_task
from task_manager.utils import create_maintenance_tasks

@shared_task
def generate_maintenance_tasks():
    create_maintenance_tasks()

from django.db import models
from django.utils.timezone import now

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    CATEGORY_CHOICES = [
        ('software', 'Software'),
        ('hardware', 'Hardware'),
        ('utility', 'Utility'),
    ]

    equipment_name = models.CharField(max_length=255)
    equipment_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    technician_name = models.CharField(max_length=255, blank=True, null=True)  # Free-text input for technician name
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=20,
        default='Pending',
        choices=[
            ('Pending', 'Pending'),
            ('Approved', 'Approved'),
            ('Completed', 'Completed'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipment_name} - {self.priority}"

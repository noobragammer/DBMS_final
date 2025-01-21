
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Technician', 'Technician'),
        ('Employee', 'Employee'),
        ('Admin', 'Admin'),
    ]

    date_of_birth = models.DateField(null=True, blank=True)
    signature = models.ImageField(upload_to='signatures/', null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Employee')
    serial_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def save(self, *args, **kwargs):
        if self.role == 'Admin' and CustomUser.objects.filter(role='Admin').exists():
            raise ValueError("There can only be one Admin account.")
        super().save(*args, **kwargs)

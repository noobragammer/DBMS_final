from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.hashers import make_password, check_password

class User(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    contact_number = models.CharField(max_length=50, null=True, unique=True)
    email_address = models.EmailField(unique=True)
    password = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(8)]
    )
    role = models.CharField(max_length=50, choices=[
        ('Admin', 'Admin'),
        ('User', 'User'),
        ('Technician', 'Technician'),
    ])  
    signature = models.ImageField(upload_to='signatures/')

    def save(self, *args, **kwargs):
        if not User.objects.exists():
            self.role = 'Admin'
        if self._state.adding or 'password' in self.get_dirty_fields():
            if not self.password.startswith('pbkdf2_'):
                self.password = make_password(self.password)
        super().save(*args, **kwargs)


    def check_password(self, raw_password):
        """
        Check if the provided password matches the hashed password stored in the database.
        """
        return check_password(raw_password, self.password)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    
    




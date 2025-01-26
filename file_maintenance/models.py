from django.db import models

class Equipment(models.Model):
    SOFTWARE = 'software'
    HARDWARE = 'hardware'
    UTILITY = 'utility'

    CATEGORY_CHOICES = [
        (SOFTWARE, 'Software'),
        (HARDWARE, 'Hardware'),
        (UTILITY, 'Utility'),
    ]

    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    YEARLY = 'yearly'

    FREQUENCY_CHOICES = [
        (WEEKLY, 'Weekly'),
        (MONTHLY, 'Monthly'),
        (YEARLY, 'Yearly'),
    ]

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]

    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    date_commission = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

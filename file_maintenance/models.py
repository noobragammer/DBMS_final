from django.db import models
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta

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
    
    def next_maintenance_date(self):
        """Calculate the next maintenance date based on the frequency."""
        if not self.date_commission:
            return None

        today = date.today()
        delta = None

        if self.frequency == self.WEEKLY:
            delta = timedelta(weeks=1)
        elif self.frequency == self.MONTHLY:
            delta = relativedelta(months=1)
        elif self.frequency == self.YEARLY:
            delta = relativedelta(years=1)

        if delta:
            next_date = self.date_commission
            while next_date <= today:
                next_date += delta
            return next_date
        return None
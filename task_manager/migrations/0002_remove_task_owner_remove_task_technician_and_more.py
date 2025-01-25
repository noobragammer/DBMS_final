# Generated by Django 5.0.6 on 2025-01-25 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='task',
            name='technician',
        ),
        migrations.AddField(
            model_name='task',
            name='technician_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

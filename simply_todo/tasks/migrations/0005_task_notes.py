# Generated by Django 5.1.7 on 2025-03-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
    ]

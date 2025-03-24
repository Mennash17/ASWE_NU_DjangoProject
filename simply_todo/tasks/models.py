from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Study', 'Study'),
        ('Personal', 'Personal'),
        ('Other', 'Other'),
    ]
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='Other')

    due_date = models.DateField(default=timezone.now)

    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    notes = models.TextField(blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

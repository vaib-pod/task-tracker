from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    is_done = models.BooleanField()
    description = models.TextField()
    due_date = models.DateField()
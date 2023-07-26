from django.db import models
from datetime import datetime

# Create your models here.
class TodoList(models.Model):
    task = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now())
from email.policy import default
from django.db import models

# Create your models here.

class task(models.Model):    
    task_data = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class task(models.Model):  
    user = models.ForeignKey(User, on_delete= models.CASCADE, null = True, blank = True)  
    task_data = models.CharField(max_length=250)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_data
    
    
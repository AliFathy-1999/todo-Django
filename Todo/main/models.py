from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.
class Todo(models.Model):
    name = models.CharField(max_length=150, blank=True , null=True)
    isCompleted = models.BooleanField(default=False)
    createdAt = models.DateTimeField( auto_now_add=True , null = True , blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank = True)
    
class TodoTasks(models.Model):
    name = models.CharField(max_length=150, blank=True , null=True)
    description  = models.TextField()
    createdAt = models.DateTimeField( auto_now_add=True )
    isCompleted = models.BooleanField(default=False)
    task = models.ForeignKey(Todo,on_delete=models.SET_NULL, null=True)
    def getDesc(self):
        return self.description[:30] 
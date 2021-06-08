from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.

class Project(TimeStampedModel):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    duration = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='profilepics/%Y/%m/%d/', default='',blank=True, null=True)
    
class Task(TimeStampedModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
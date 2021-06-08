from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()
    duration = models.CharField(max_length=300)
    avatar = models.ImageField(upload_to='profilepics/%Y/%m/%d/', default='',blank=True, null=True)
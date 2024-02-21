from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse 

# Create your models here.
class note(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('notes-update',kwargs={'pk':self.pk})


class user(models.Model):
    username=models.CharField(max_length=15)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.username
    
##to tell django how to get the url of any instance of a note
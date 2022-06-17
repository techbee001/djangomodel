from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()

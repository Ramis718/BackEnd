from django.db import models
from enum import auto
from django.db import models
from django.db.models.fields import TextField

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField() #нет ограничений
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)

class Coment(models.Model):
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

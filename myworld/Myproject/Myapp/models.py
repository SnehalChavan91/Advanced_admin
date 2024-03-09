from django.db import models
from datetime import datetime
from django.utils import timezone
# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=50,default="abcd")
    age=models.IntegerField
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    color_code=models.CharField(max_length=6)
    birthday=models.DateField()

class Author(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=3,default="Mr")
    birth_date=models.DateField()
    pub_date=models.DateField(default=timezone.now())

    def __str__(self):
        return f"{self.name}{self.birth_date}"
    

class Reader(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    favourite_author=models.ManyToManyField('Author')

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

class Editor(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    edited_authors=models.ManyToManyField('Author')

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
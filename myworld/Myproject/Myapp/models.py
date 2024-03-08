from django.db import models

# Create your models here.
class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    biography=models.TextField
    date_of_birth=models.DateField()
    pub_date=models.DateField()

    def __str__(self):
        return f"{self.first_name}{self.last_name}"
    

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
from django.db import models

class Restaurant(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    food = models.CharField(max_length=100)

class Profile(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)

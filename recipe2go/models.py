from django.db import models

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=250)

class Videos(models.Model):
    id = models.AutoField(primary_key=True)
    length = models.CharField(max_length=250)

class Invocations(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    product = models.ManyToManyField(Videos)

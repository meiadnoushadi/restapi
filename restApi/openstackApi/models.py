from django.db import models

# Create your models here.
class Openstack(models.Model):
    name=models.CharField(max_length=200)
    password=models.CharField(max_length=300)
    nameProject=models.CharField(max_length=300)
    
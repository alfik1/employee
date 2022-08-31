from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department=models.CharField(max_length=50)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()

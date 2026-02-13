from django.db import models

# Create your models here.
# Script: student/models.py
from django.db import models

class Student(models.Model):
    studentName= models.CharField(max_length=100)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    def __str__(self):
        return self.name


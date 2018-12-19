from django.db import models

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()
    class Meta:
        db_table='student'
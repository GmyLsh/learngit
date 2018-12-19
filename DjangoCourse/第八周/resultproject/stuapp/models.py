from django.db import models

# Create your models here.
class StuModel(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
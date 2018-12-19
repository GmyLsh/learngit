from django.db import models

# Create your models here.
class UserModel(models.Model):
    uname = models.CharField(max_length=20)
    upassword = models.CharField(max_length=50)

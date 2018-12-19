from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=50,null=True,default=None)
    address=models.CharField(max_length=100)
    #TextField():不限制内容长度
    message=models.TextField()
    class Meta:
        db_table='message'
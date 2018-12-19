from django.db import models

# Create your models here.

class PModel(models.Model):
    pic_url=models.ImageField(upload_to='upload/%Y/%m')

    def __str__(self):
        return self.pic_url.name

    class Meta:
        db_table='pic'
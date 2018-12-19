from django.db import models

# Create your models here.
class PictureModel(models.Model):
    #该字段用于保存图片上传之后的地址。
    #upload_to:知名图片在MEDIA_ROOT目录下的具体存放目录。如果不指定这个参数，默认所有的图片都保存在MEDIA_ROOT目录下。/static/media/imguploadapp/1.jpg
    #upload_to如果指定了目录，这个目录需要自己手动创建。但是在这里通过表单上传这个(ImageField(upload_to='imguploadapp'))没用,admin后台可以这样，这个表单上传不需要。

    pic_url=models.ImageField(upload_to='imguploadapp')

    # def __str__(self):
    #     return self.pic_url.name

    class Meta:
        db_table='picture'

from django.db import models

# Create your models here.
#如何将图片上传到自定义目录下。


class Picture(models.Model):
    #upload_to:在指定目录下(/static/images/)要生成的目录。
    #MEDIA_ROOT:只要上传图片，肯定要设置的。用于指定图片的上传的根目录。可以设置在static下(static目录的搜索路径，已经通过STATICFILES_DIRS配置过了)，也可以自定义目录(MEDIA_URL)。
    pic_url=models.ImageField(upload_to='%Y/%m')

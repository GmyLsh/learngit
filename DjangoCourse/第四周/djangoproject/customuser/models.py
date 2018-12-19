from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModels(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, verbose_name='用户昵称')
    mobile = models.CharField(max_length=11, null=True, verbose_name='电话')
    address = models.CharField(max_length=100, null=True, verbose_name='住址')
    sex = models.CharField(max_length=10, null=True, verbose_name='性别')
    head_img = models.ImageField(upload_to='%Y/%m', verbose_name='头像', null=True)
    """
    0-普通用户
    1-黄金会员(50)
    2-超级会员(100)
    """
    roles=models.IntegerField(default=0,verbose_name='用户等级')

    class Meta:
        db_table = 'user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

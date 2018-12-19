from django.db import models
from django.contrib.auth.models import AbstractUser
#Django框架将createsuperuser创建的用户以及在admin后台添加的用户，默认都保存在了auth_user这个表中，但是这个表的字段是固定的，如果想给用户扩展一些字段(年龄、性别、住址等)，就需要重写User表了，不能再使用auth_user这个表了.

class UserModel(AbstractUser):
    """
    AbstractUser这个类，也就是Django框架默认使用的一个用于管理用户的User类，这个类生成一个auth_user表。所以，要扩展用户属性，可以继承AbstractUser，在子类UserModel中实现扩展。
    注意:要使用自定义user表，需要在settings.py中配置AUTH_USER_MODEL，否则Django是无法识别这个UserModel的；
    """
    nick_name=models.CharField(max_length=20,verbose_name='用户昵称')
    address=models.CharField(max_length=150,verbose_name='家庭住址')
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name
        db_table='user'


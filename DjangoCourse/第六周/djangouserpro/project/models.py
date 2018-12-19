from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModels(AbstractUser):
    nickname = models.CharField(max_length=50, null=True, verbose_name='用户昵称')
    mobile = models.CharField(max_length=11, null=True, verbose_name='电话')
    address = models.CharField(max_length=100, null=True, verbose_name='住址')
    sex = models.CharField(max_length=10, null=True, verbose_name='性别')

class EmailCodeModel(models.Model):
    """
    作用:在发送激活邮件时，后台会先生成一个随机字符产，然后将这个随机字符串保存在这个model中，同时将这个随机字符串以激活链接的形式，发送到用户邮箱；当用户点击这个激活链接时，会将这个随机字符串再次传递到后台的视图函数中，后台会使用这个随机字符串去该Model对应的表中查询是否存在，如果存在，说明可以激活，如果不存在则激活失败。
    """
    code=models.CharField(max_length=100)
    #这个激活码记录中，既要保存激活码(随机字符串)又要保存该激活码对应的邮箱是哪一个。
    email=models.EmailField()
    #记录激活邮件的发送时间
    send_time=models.DateTimeField(auto_now_add=True)
    #邮件发送的类型:激活邮件、找回密码
    send_type=models.CharField(choices=(('register','激活'),('forget','忘记密码')),max_length=30)
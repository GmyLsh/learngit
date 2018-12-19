from django.db import models

# Create your models here.

#admin管理后台:是Django提供的一套用于管理用户和数据的wed系统，通过它可以很方便的实现数据的增删改查功能。实现对用户的管理。
class Article(models.Model):
    a_title=models.CharField(max_length=100,verbose_name='标题')
    a_content=models.TextField(verbose_name='内容')
    a_author=models.CharField(max_length=20,verbose_name='作者')
    #editable=True:让自动生成的时间可以修改
    a_publish_date=models.DateTimeField(auto_now_add=True,editable=True,auto_created=True,verbose_name='发布时间')
    a_update=models.DateTimeField(auto_now=True,verbose_name='更新时间')
    def __str__(self):
        #这个函数仅适合admin.site.register(Article)这种注册形式。
        #相当于给model对象添加一个默认值，当结果是一个对象object的时候，直接显示self.a_title的值。否则直接显示xxx object
        return self.a_title

    class Meta:
        #Meta是用于设置Model级别的对象配置。
        db_table='article'
        #英文单词单数使用verbose_name
        verbose_name='文章'
        #英文单词复数(s)使用verbose_name_plural
        verbose_name_plural='文章'

"""
1.创建Model类，并同步至mysql数据库；
2.通过命令python manage.py createsuperuser创建超级管理员，输入用户名和密码，邮箱可以为空；密码不能太过于简单，否则无法创建成功，密码至少是8位的字母数字组合；
3.配置admin.py文件
4.运行访问即可；
"""
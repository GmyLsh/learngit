from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
"""
分类:分类名称、分类的排序
广告:广告标题、广告地址、图片路径
文章:文章标题、文章描述、文章内容、标签
标签:军事、经济、IT
用户
"""
class Article(models.Model):
    a_title=models.CharField(max_length=20,verbose_name='文章标题')
    a_content=models.CharField(max_length=100,verbose_name='文章内容')
    a_label=models.CharField(max_length=20,verbose_name='标签')
    a_publish_date=models.DateTimeField(auto_now_add=True,editable=True,auto_created=True,verbose_name='创建时间')
    a_look=models.IntegerField(null=True,verbose_name='浏览量')
    a_comment=models.IntegerField(null=True,verbose_name='评论数')
    def __str__(self):
        return self.a_title
    class Meta:
        db_table='article'
        verbose_name='文章'
        verbose_name_plural=verbose_name
class Advertising(models.Model):
    AD_title=models.CharField(max_length=20,verbose_name='广告标题')
    AD_address=models.CharField(max_length=50,verbose_name='广告地址')
    AD_img_url=models.ImageField(upload_to='images')

    def __str__(self):
        return self.AD_title
    class Meta:
        db_table='AD'
        verbose_name='广告'
        verbose_name_plural=verbose_name
class Label(models.Model):
    a_label=models.CharField(max_length=20,verbose_name='标签')
    def __str__(self):
        return self.a_label
    class Meta:
        db_table='label'
        verbose_name='标签'
        verbose_name_plural=verbose_name
class Sort(models.Model):
    a_sort_name=models.CharField(max_length=20,verbose_name='分类名称')
    a_sort=models.IntegerField(null=True,verbose_name='排序')
    def __str__(self):
        return self.a_sort_name
    class Meta:
        db_table='sort'
        verbose_name='分类'
        verbose_name_plural=verbose_name
class User(AbstractUser):
    nickname=models.CharField(max_length=20,null=True,verbose_name='用户昵称')
    mobile=models.CharField(max_length=20,null=True,verbose_name='电话')
    address=models.CharField(max_length=100,null=True,verbose_name='住址')
    head_img=models.ImageField(upload_to='img/%Y/%m',verbose_name='头像',null=True)
    class Meta:
        db_table='user'
        verbose_name='用户'
        verbose_name_plural=verbose_name
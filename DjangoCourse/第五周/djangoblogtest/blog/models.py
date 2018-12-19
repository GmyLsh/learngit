from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    header=models.ImageField(upload_to='user/%Y/%m',blank=True,null=True,verbose_name='头像')
    class Meta:
        verbose_name='用户'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.username

class Tag(models.Model):
    name=models.CharField(max_length=20,verbose_name='标签名称')
    class Meta:
        verbose_name='标签'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=20,verbose_name='分类名称')
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.name



class ArticleManager(models.Manager):
    def archive_date(self,article_list):
        archive_list=[]
        # 需要获取所有的文章model对象。
        for article in article_list:
            # 将每一个文章的发布日期都获取出来，按照'%Y/%m'进行格式化
            pub_date = article.date_publish.strftime('%Y/%m')
            if pub_date not in archive_list:
                # 如果这个时间字符串不在article_list这个列表里面就把这个年月添加进去
                archive_list.append(pub_date)
        return archive_list



class Article(models.Model):
    objects=ArticleManager()
    title=models.CharField(max_length=100,verbose_name='文章标题')
    desc=models.CharField(max_length=100,verbose_name='文章简介')
    content=models.CharField(max_length=100,verbose_name='文章内容')
    click_num=models.IntegerField(verbose_name='点击量',default=0,editable=True)
    comment_num=models.IntegerField(verbose_name='评论量',default=0,editable=True)
    date_publish=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    tag=models.ManyToManyField(Tag,verbose_name='所属标签')
    category=models.ForeignKey(Category,verbose_name='所属分类',on_delete=models.DO_NOTHING,blank=True,null=True)
    class Meta:
        verbose_name='文章'
        verbose_name_plural=verbose_name
        ordering=['-date_publish']
    def __str__(self):
        return self.title


class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.DO_NOTHING,verbose_name='所属文章')
    content=models.CharField(max_length=200,verbose_name='评论内容')
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content

class Ad(models.Model):
    title=models.CharField(max_length=100,verbose_name='广告标题')
    desc=models.CharField(max_length=200,verbose_name='广告简介')
    image=models.ImageField(upload_to='ad/%Y/%m',verbose_name='图片')
    date_publish=models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    class Meta:
        verbose_name='广告'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.title







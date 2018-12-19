from django.db import models

# Create your models here.
class Publication(models.Model):
    name=models.CharField(max_length=20,verbose_name='出版社')
    creater_time=models.DateTimeField(null=True,verbose_name='创立时间',auto_now_add=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='出版社'
        verbose_name_plural=verbose_name

class Book(models.Model):
    name=models.CharField(max_length=20,verbose_name='图书名称')
    #max_digits=5:表示这个小数数字(不算那个点)的整体个数(整数+小数)
    #decimal_places=2:小数位的个数
    price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name='图书价格')
    level=models.CharField(max_length=20,verbose_name='图书级别')
    publication=models.ForeignKey(Publication,related_name='book',null=True,on_delete=models.DO_NOTHING,verbose_name='出版社')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='图书'
        verbose_name_plural=verbose_name
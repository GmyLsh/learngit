from django.db import models

# Create your models here.
#多对多：一个表中的一条数据对应另一个表中的多条数据；另外一个表中的一条数据对应着签一个表中的多条数据；
class Publication(models.Model):
    """
    出版社(主表)
    """
    p_name=models.CharField(max_length=50)

class Article(models.Model):
    """
    文章(从表)
    """
    a_name=models.CharField(max_length=50)
    pub=models.ManyToManyField(Publication)
#一对多:ForginKey一定要设置在从表。
#一对一和多对多:关系可以设置在任意一个列表中。
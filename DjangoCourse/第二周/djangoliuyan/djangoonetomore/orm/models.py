from django.db import models

# Create your models here.
class NewsType(models.Model):
    """
    新闻类型(军事、娱乐)
    """
    type_name=models.CharField(max_length=20)
    class Meta:
        db_table='new_type'
class NewsTag(models.Model):
    """
    新闻类标签(实时、热点)
    """
    type_name=models.CharField(max_length=20)
    class Meta:
        db_table='new_name'
class NewsAuthor(models.Model):
    """
    新闻作者()
    """
    type_name=models.CharField(max_length=20)
    class Meta:
        db_table='new_author'
class News(models.Model):
    """
    新闻
    """
    new_name=models.CharField(max_length=100)
    new_content=models.TextField()

    news_type=models.ForeignKey(NewsType,on_delete=models.CASCADE)
    news_tag=models.ForeignKey(NewsTag,on_delete=models.CASCADE)
    news_author=models.ForeignKey(NewsAuthor,on_delete=models.CASCADE)

    class Meta:
        db_table='news'

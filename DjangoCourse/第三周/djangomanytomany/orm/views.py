from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
    #添加
    #一对一和一对多:先添加主表的数据，再添加从表的数据；
    #多对多:先添加两个表的数据，然后在进行关联；
    # p1=Publication(p_name='新华出版社')
    # p1.save()
    # p2=Publication(p_name='东方出版社')
    # p2.save()
    #
    # a1=Article(a_name='个税改革')
    # a1.save()
    # a2=Article(a_name='大桥通车')
    # a2.save()
    #
    # #关联文章和出版社的关系
    # #a1这个文章关联的出版社是p1和p2，意思就是p1和p2两个出版社都出版了a1这个文章。
    # a1.pub.add(p1,p2)
    # a2.pub.add(p2)


    #查询:
    #1-根据主表数据查询从表数据
    p1=Publication.objects.get(id=2)
    articles=p1.article_set.all()
    for article in articles:
        print(article.a_name)
    #2-根据从表数据查询主表数据
    #查询"个税改革"这个文章，共有几个出版社出版；
    a1=Article.objects.get(id=1)
    pubs=a1.pub.all()
    for p in pubs:
        print(p.p_name)
    return HttpResponse('数据添加成功')

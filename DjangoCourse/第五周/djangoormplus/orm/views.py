from django.shortcuts import render
from .models import *
from datetime import date
from django.http import HttpResponse
# Create your views here.
def select(request):
    #1.单表数据查询。
    #id__lt=3小于,id__gt=1大于 查询id>1且id<3的所有出版社。
    #id__lte:小于等于，id__gte:大于等于
    results=Publication.objects.filter(id__lt=3,id__gt=1)
    #查询id=1,2的出版社
    results=Publication.objects.filter(id__in=[1,2])
    #查询id!=1的出版社 exclude():取反
    results=Publication.objects.exclude(id__in=[1])
    #包含关系查询:比如查询出版社中含有"新"字的所有出版社。
    results=Publication.objects.filter(name__contains='新')
    """
    name__startswith("新"):查询name字段的值以"新"字开头的所有Model对象;
    name__endswith("新"):查询name字段的值以"新"字结尾的所有Model对象;
    name__istartswith("J"):查询name字段的值以"J"字开头的所有Model对象;(如果值是英文，忽略大小写)
    """
    #查询2018年的所有数据
    results=Publication.objects.filter(creater_time__year=2018)
    #查询某一个时间范围内的数据
    start_time=date(2018,10,1)
    end_time=date(2018,11,30)
    results=Publication.objects.filter(creater_time__range=(start_time,end_time))
    #查询2018年以后的数据
    start_time=date(2018,1,1)
    results=Publication.objects.filter(creater_time__gt=start_time)
    for result in results:
        print(result.name)
    return HttpResponse('ok')

#引入Django内置的统计函数：求平均值、最大值、最小值、组内数据个数、求和
from django.db.models import Avg,Max,Min,Count,Sum,F,Q
def annotate(request):
    """
    数据分组查询：指的就是根据某一个表中的字段，对所有的数据进行分组，然后在对分组之后的数据进行操作。
    :param request:
    :return:
    """

    #单表的分组查询
    #图书表：Book。将图书表中的所有数据按照图书的级别进行分组，统计每一个分组中的数据个数。
    #Book.objects.values('level'):将数据按照level的值进行分组，分组以后，再调用annotate进行数据的统计。
    #<QuerySet [{'level': '高级', 'level__count': 3}, {'level': '初级', 'level__count': 1}, {'level': '中级', 'level__count': 3}]>
    result=Book.objects.values('level').annotate(Count('level'))


    #先按照级别分组，再统计每一个分组的价格平均值。
    #<QuerySet [{'level': '高级', 'price__avg': 90.0}, {'level': '初级', 'price__avg': 22.0}, {'level': '中级', 'price__avg': 90.0}]>
    #price__ave:价格字段price+统计函数Avg共同组成这个键。
    result=Book.objects.values('level').annotate(Avg('price'))



    #自定义键avg_price
    #<QuerySet [{'level': '高级', 'avg_price': 90.0}, {'level': '初级', 'avg_price': 22.0}, {'level': '中级', 'avg_price': 90.0}]>
    result = Book.objects.values('level').annotate(avg_price=Avg('price'))


    #先按照级别分组，再统计每一个分组的个数，最后再按照个数进行升序/降序排列。若是没有指定键count，则写默认的price__avg
    result=Book.objects.values('level').annotate(count=Count('level')).order_by('count').values('level','count')
    for r in result:
        print("12344",r)

    #2.多表查询
    #查询Book表，按照出版社进行分组，然后再统计这个出版社出版的图书的个数。
    result=Book.objects.values('publication').annotate(count=Count('publication'))

    #1.
    result=Publication.objects.annotate(Minprice=Min('book__price'))
    for publish in result:
        print(publish.name,publish.Minprice)
    #2.
    results=Publication.objects.annotate(countnum=Count('book__level'))
    for result in results:
        if result.countnum>1:
            print(result,result.countnum)
            res=Book.objects.filter(publication=result).values_list('id','name','price','level')
            print(res)

    #3.
    results=Publication.objects.annotate(SumPrice=Sum('book__price'))
    for result in results:
        print(result,result.SumPrice)

    # a.统计每一个出版社中价格最低的图书；
    result=Book.objects.values('publication').annotate(min_price=Min('price'))
    # b.统计出出版社出版图书数量大于1的图书的信息；
    result=Book.objects.values('publication').annotate(count=Count('publication')).filter(count__gt=1)
    # c.统计每一个出版社，出版的所有图书的总价格；
    result=Book.objects.values('publication').annotate(sum_price=Sum('price'))

    #聚合函数(aggregate():聚合指的就是将一些分散的数据、零散的数据，通过"分类-分析-统计整理"得到数据的过程就称为聚合。)
    #Avg，Max，Min，Count，Sum:聚合函数。
    result=Book.objects.all().aggregate(price=Count('price'))
    result=Book.objects.all().aggregate(price=Avg('price'))
    print(result)
    #Q对象查询:查询条件有"或"出现的情况；
    #查询出版社id=1或者id=3的出版社
    result=Publication.objects.filter(Q(id=1)|Q(id=3))

    #Q也支持&且查询Q(id=1)&Q(id=3),和filter(id=1,name="新东方")一样的意思。

    #~Q():取反：
    #比如:查询图书信息，要求该图书的出版社id=4且图书名称不是"html5"的图书信息；
    result=Book.objects.filter(Q(publication_id=4)&~Q(name='html5'))
    print(result)
    return HttpResponse('ok')

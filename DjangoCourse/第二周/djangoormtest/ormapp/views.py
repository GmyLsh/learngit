from django.shortcuts import render
from .models import Person
from django.http import HttpResponse
# Create your views here.
"""
Django框架的数据库操作：这里的数据库操作并没有采用原始的sql语句形式，而是采用了ORM技术实现数据的增删改查。这里的ORM指的是对象关系映射(Object Relational Mapping），它是将表与表之间的关系映射为了对象与对象的关系，在这里操作对象就是在操作表。所有表的增删改查都是基于对象来完成的。
关系型数据库:多表联查。表与表之间的关系非常重要，表关系映射变成对象关系映射。

通过这种关系操作数据库，可以有效地防止SQL语句注入的风险。
insert into;
delete from student;
() values ();
"""
def insert_data(request):
    #第一种添加数据
    Person.objects.create(user_name='陈罗文',user_height=165)
    #第二种添加数据
    # p=Person(user_name='陈小鸡')
    # p.save()
    #第三种添加数据
    # p=Person()
    # p.user_name='陈小罗'
    # p.user_height=165
    # p.save()
    #第四种添加数据
    #在创建新的数据之前，先查询数据库中是否已经存在对应的数据，如果已经存在就不在创建这个对象了。可以起到一定的去重作用。
    Person.objects.get_or_create(user_name='li',user_height=180)

    return HttpResponse('数据添加成功')
def select_data(request):
    #数据的查询
    #1.单条数据查询:get(),参数就是查询条件，可以是类中的属性。
    # p=Person.objects.get(user_name='li')
    #2.多条数据的查询:filter(),参数就是查询条件，查询结果是一个列表。
    # p=Person.objects.filter(user_height=170)
    #3.查询所有数据:all(),返回值也是一个结果集QuerySet
    # p=Person.objects.all()
    # return render(request,'index.html',{'p':p})

    #数据修改
    p=Person.objects.get(user_name='li')
    p.user_height=80
    p.save()

    #update():参数就是更新的数据。这个函数是更新所有的数据。
    Person.objects.update(user_height=200)

    #数据删除
    Person.objects.get(user_name='li').delete()

    return HttpResponse('数据修改成功！')
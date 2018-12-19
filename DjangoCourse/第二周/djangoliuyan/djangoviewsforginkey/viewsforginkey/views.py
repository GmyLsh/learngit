from django.shortcuts import render
from django.views.generic import View
from .models import Classes,Student
# Create your views here.
#通用视图的用法
#1.主要作用还是用于配置url路由，只不过形式和视图函数写法不一样，但是功能是一样的:视图函数区分GET和POST主要是通过request.method，而通用视图将GET和POST请求封装成了类中的两个方法；

class Home(View):
    def get(self,request,id):
        print('====',id)
        """
        self和request是固定的两个参数，这两个参数后面如果还有参数，那就是url传递的参数；
        :param request:
        :return:
        """
        return render(request,'index.html')
    def post(self,request,id):
        print('---',id)
        a=request.POST.get('a')
        b=request.POST.get('b')

        return render(request,'index.html',{'result':int(a)+int(b)})
class DataHandler(View):
    def get(self,request):
        #数据库中要先存在主表的数据，然后才能创建从表的数据。
        # c1=Classes(c_name='1班')
        # c1.save()
        # c2=Classes(c_name='2班')
        # c2.save()
        # c3=Classes(c_name='3班')
        # c3.save()
        #
        # #关联主表id:通过classes(表面)或者classes_id都可以进行绑定
        # s1=Student(s_name="张三",classes_one=c1,classes_two=c1)
        # s1.save()
        # s1=Student(s_name='张三',classes=c1)
        # s1.save()
        # s2=Student(s_name="李四",classes_id=c1.id)
        # s2.save()
        # s3 = Student(s_name="王五", classes=c2)
        # s3.save()
        # s4 = Student(s_name="赵六", classes_id=c3.id)
        # s4.save()
        # return render(request,'index.html')
        #如何根据主表的一条数据查询所有从表的数据?
        c1=Classes.objects.get(id=1)
        # #语法:主表数据.从表名称_set
        # #student_set就是一个查询结果集，所有学生都在里面。
        # stus=c1.student_set.all()
        #
        #如果从表出现，多个关联同一个朱标的外键，就不能在使用student_set了，无法区分是classes_one还是classes_two
        stus=c1.cls_one.all()
        # #如何根据从表的一条数据查询对应的一条主表的数据?
        s1=Student.objects.get(id=1)
        # #classes就是s1对象的属性，是在Student类中声明的一个属性。
        classes_name=s1.classes.c_name
        # return render(request,'index.html',{'stus': stus, 'c1': c1, 's1': s1, 'name': classes_name})
        return render(request,'index.html',{'stus':stus})
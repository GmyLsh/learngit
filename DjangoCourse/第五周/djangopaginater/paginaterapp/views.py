from django.shortcuts import render
from django.http import HttpResponse
from .models import User
# Create your views here.
def add(request):
    for x in range(1,101):
        name='张三%s'%x
        age=20 + x

        user=User(name=name,age=age)
        user.save()
    return HttpResponse('ok')
from django.core.paginator import PageNotAnInteger,Paginator,InvalidPage,EmptyPage
def select(request):
    #1.把需要分页的数据全部查询出来；
    user_list=User.objects.all()
    #2.利用user_list数据，创建一个分页器对象
    #参数1:要分页得数据，参数2:设置每页要展示的数据个数；参数3：如果最后一页不到5个数据，是否将最后一页数据合并到上一页进行展示；默认是False，不合并；
    paginator=Paginator(user_list,5)
    #3.创建页面对象page，每一个page对应的是每一个页面，这个page中包含:
    #a> page.number:表示当前查询的页码
    #b> page.object_list:表示当前页要展示的数据；
    #c>page.paginator:它就是上面创建的Paginator(user_list,5)这个对象，无论是哪一页，这个paginator对象始终跟着Page对象；
    try:
        page_number=request.GET.get('page','1')
        page=paginator.page(page_number)
    except (PageNotAnInteger,EmptyPage,InvalidPage):
        #如果出现上述异常，默认展示第1页
        page = paginator.page(1)
    return render(request,'index.html',{'page':page})

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def add(request):
    return HttpResponse('你访问了第一个url路由')
def add1(request,a,b):
    return HttpResponse('结果是:{}'.format(a+b))
def get_url(request):
    #reverse()这个函数就是根据url路由的name参数，来反向获取url地址的方法。
    #所以，url路由的name参数不仅仅可以在模板中使用{% url 'add' %},也可以在views.py中使用。
    result=reverse('add1',args=('456','123'))
    return HttpResponse(result)
def index(request):
    return render(request,'index.html')
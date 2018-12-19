from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#Django框架在调用index的时候会传递过来一个请求对象request赋值给这个形参。
def index(request):
    return HttpResponse('这是一aa个测试')

def base_index(request):
    return HttpResponse('这是base这个app应用的首页')
def base_list(request):
    return HttpResponse('这是base这个app应用的列表页')
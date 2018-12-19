from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('这是一个测试')

def base2_index(request):
    return HttpResponse('这是base2这个app应用的首页')
def base2_list(request):
    return HttpResponse('这是base2这个app应用的列表页')
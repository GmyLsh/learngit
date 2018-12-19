from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def params_firse(request):
    #针对路由的第一种情况，直接从GET请求中获取参数。
    user_name=request.GET.get('user','')
    pass_word=request.GET.get('pwd','')
    result='账号：{}，密码：{}'.format(user_name,pass_word)
    return HttpResponse(result)
def params(request,name,pwd):
    result='name={},pwd={}'.format(name,pwd)
    return HttpResponse(result)
def params1(request,username,password):
    result = 'name==={},pwd==={}'.format(username, password)
    return HttpResponse(result)
def params2(request,user,pwd):
    result = 'name={},pwd={}'.format(user, pwd)
    return HttpResponse(result)
def params3(request,id,username):
    result = 'id={},name={}'.format(id,username)
    return HttpResponse(result)
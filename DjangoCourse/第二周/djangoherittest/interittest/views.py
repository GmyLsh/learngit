from django.shortcuts import render

# Create your views here.
def zhichang(request):
    return render(request,'zhichang.html',{'type':'职场','categroy':'WEB'})
def database(request):
    return render(request,'database.html',{'type':'数据库','categroy':'python'})
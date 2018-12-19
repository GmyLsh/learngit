from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    #访问首页，页面中展示所有学员的信息。
    stus=Student.objects.all()
    if stus:
        #如果结果集存在，将这个结果集渲染到模板中。
        return render(request,template_name='index.html',context={'students':stus})
    else:
        return render(request,template_name='index.html',context={'message':'暂无学员信息'})
def add(request):
    if request.method=="GET":
        return render(request,'add.html')
    elif request.method=="POST":
        name = request.POST.get('sname')
        age = request.POST.get('sage')
        s=Student(sname=name,sage=age)
        s.save()
        return render(request,'add.html',{'result':'学员添加成功!'})
def delete(request):
    if request.method=="GET":
        return render(request,'delete.html')
    elif request.method=="POST":
        #接收学员ID值，去数据库中查询数据
        stu_id=request.POST.get('sname')
        try:
            Student.objects.get(id=stu_id).delete()
            return render(request,'delete.html',{'message':'删除id={}学员成功！'.format(stu_id)})
        except:
            return render(request,'delete.html',{'message':'没有查到id={}相关信息!'.format(stu_id)})
def select(request):
    if request.method=="GET":
        return render(request,'select.html')
    elif request.method=="POST":
        #接收学员ID值，去数据库中查询数据
        stu_id=request.POST.get('sname')
        student=Student.objects.get(id=stu_id)
        if student:
            return render(request,'select.html',{'student':student})
        else:
            return render(request,'select.html',{'message':'没有查到id={}相关信息!'.format(stu_id)})
from django.shortcuts import render,reverse
from .models import Message
# Create your views here.
def list(request):
    return render(request,'list.html',{'messages':Message.objects.all()})
def add(request):
    if request.method=='GET':
        #第一种写法
        # return render(request, 'add.html', {'url_name': '/add/'})
        #第二种写法
        # 在views.py中使用name反射url地址。
        url = reverse('add')
        return render(request,'add.html',{'url_name':url,'value': '添加'})
    elif request.method=='POST':
        #通过表单添加数据
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        message=request.POST.get('message')

        m=Message()
        m.name=name
        m.email=email
        m.address=address
        m.message=message
        m.save()
        return render(request,'add.html',{'result':'数据添加成功！','value': '添加'})
def update(request):
    if request.method=='GET':
        #第一种写法
        # return render(request,'update.html',{'url_name':'/update/'})
        url=reverse('update')
        return render(request, 'update.html', {'url_name': url, 'value': '修改'})
    elif request.method=='POST':
        #通过表单修改数据
        m_id=request.POST.get('id')
        try:
            m=Message.objects.get(id=m_id)
            m.name=request.POST.get('name')
            m.email = request.POST.get('email')
            m.address = request.POST.get('address')
            m.message = request.POST.get('message')
            m.save()
            return render(request,'update.html',{'result':'数据修改成功！', 'value': '修改'})
        except:
            return render(request,'update.html',{'result': '该用户不存在！', 'value': '修改'})
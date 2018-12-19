from django.shortcuts import render
from .models import Account,Contact
from datetime import datetime
# Create your views here.
def add(request):
    #添加
    a1=Account(a_name='1@qq.com',a_pwd='123',a_register_date=datetime.now(),a_update_date=datetime.now())
    a1.save()
    a2 = Account(a_name='2@qq.com', a_pwd='456', a_register_date=datetime.now(), a_update_date=datetime.now())
    a2.save()
    #添加从表数据
    c1=Contact(c_name='张三',c_address='北京',c_phone='110',account=a1)
    c1.save()
    c2 = Contact(c_name='李四', c_address='江南', c_phone='119', account_id=a2.id)
    c2.save()
    return render(request,'index.html',{'result':'数据添加成功'})

def select(request):
    #根据主表的一条数据，查询从表的一条数据。也就是查询该账户的拥有人是谁
    account=Account.objects.get(id=2)
    contact=account.contact.c_name
    #根据从标的一条数据，查询主表的一条数据。也就是查询这个人的账户
    contact=Contact.objects.get(id=2)
    account=contact.account.a_name
    return render(request,'index.html',{'data':account})
def update(request):
    account=Account.objects.get(id=1)
    account.a_pwd='110'
    account.save()
    return render(request,'index.html',{'result':'数据修改成功'})
def delete(request):
    Account.objects.get(id=1).delete()
    return render(request,'index.html',{'result':'数据删除成功'})
from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from stage.models import Stage
from .models import Outline
# Create your views here.
class OutlineListView(View):
    def get(self,request):
        #要获取所有的大纲信息，需要获取当前的阶段stage。
        stage=Stage.objects.get(id=request.GET.get('stage_id'))
        value=request.GET.get('value')
        ols=stage.outline_set.all()
        return render(request,'outline/list.html',locals())

class OutlineAddView(View):
    def get(self,request):
        #在渲染添加页面的时候需要给添加页面传递一个stage对象或者stage_id。目的是在点击提交按钮的时候可以将stage_id传递给post请求中。
        stage_id=request.GET.get('stage_id')
        value=request.GET.get('value')
        return render(request,'outline/add.html',locals())
    def post(self,request):
        #获取表单数据
        stage_id=request.POST.get('stage_id')
        #需要获取stage_id，需要表明当前大纲是给哪一个阶段添加的。
        outline=Outline.objects.create(title=request.POST.get('title'),number=request.POST.get('number'),advancing=request.POST.get('advancing'),stage_id=stage_id)
        outline.save()
        #重定向到列表页
        return redirect(reverse('ol_list')+'?stage_id={}&value={}'.format(stage_id,value))

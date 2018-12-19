from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from subject.models import Subject
from .models import Stage
# Create your views here.
class StageListView(View):
    def get(self,request):
        """
        在列表页显示某一个学科对应的所有阶段。
        :param request:
        :return:
        """
        subject=Subject.objects.filter(id=request.GET.get('subject_id')).first()
        #由主表的一条数据subject，查询出从表的多条数据stages。
        stages=subject.stage_set.all()
        return render(request,'stage/list.html',locals())

    def post(self,request):
        pass

class StageAddView(View):
    """
    添加阶段信息，需要获取学科，要表明当前阶段属于哪一个学科。阶段关联的有学科的外键。
    """
    def get(self,request):
        subject = Subject.objects.filter(id=request.GET.get('subject_id')).first()
        return render(request,'stage/add.html',{'subject':subject})
    def post(self,request):
        subject_id=request.POST.get('subject_id')
        stage=Stage.objects.create(title=request.POST.get('title'),project=request.POST.get('project'),number=request.POST.get('number'),creater=request.user,updater=request.user,subject_id=subject_id)
        stage.save()
        #信息保存完成，重定向到stage/list.html
        return redirect(reverse('stage_list')+'?subject_id={}'.format(subject_id))
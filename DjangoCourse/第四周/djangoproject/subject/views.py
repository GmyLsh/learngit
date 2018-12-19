import time,datetime
from django.shortcuts import render,redirect,reverse
from .models import Subject
from django.views.generic import View
from django.contrib.auth.views import login_required
from django.utils.decorators import method_decorator
from customuser.views import manage_promessions
#Python内置的一些包的引入写在最上方，import在前，from..import..在后。
#下面用于引入自定义的一些包或者引入第三方包。
# Create your views here.
class SubjectlistView(View):
    """
    用于展示"学科"首页的通用视图。该页面中要展示所有用户添加的所有学科的信息。
    """
    def get(self,request):
        #查出来的所有数据会按照ording=['number']的要求进行排序返回。所以此时subject这个QuerySet集合就是排序之后的subject学科对象。
        subjects=Subject.objects.all()
        #locals()这个函数可以将当前函数内部所有的局部变量都传递到模板中，就不需要再拼接{'subject':subject}。
        return render(request,'subject/list.html',locals())
class SubjectAddView(View):
    """
    该视图是用来展示添加学科的页面subject/add.html,以及处理学科的添加逻辑。
    """
    @method_decorator(login_required)
    def get(self,request):
        return render(request,'subject/add.html')
    @method_decorator(login_required)
    def post(self,request):
        subject=Subject()
        subject.name=request.POST.get('name')
        subject.amount = request.POST.get('amount')
        subject.days = request.POST.get('days')
        subject.number = request.POST.get('number')

        #保存学科之前，先判断学科是否已经存在。
        result=Subject.objects.filter(name=subject.name)
        if result:
            error={'code':'该学科已经存在'}
            #数据库已经存在改名称的学科
            return render(request,'subject/add.html',locals())
        #保存成功，切换url，进入/subject/list/首页，展示所添加的学科信息。
        # 给学科添加创建人和更新人对应的用户。默认都是当前登录用户。
        subject.creater = request.user
        subject.updater = request.user
        subject.save()
        return redirect(reverse('subject_list'))
class SubjectDetailView(View):
    """
    展示学科详情页的通用视图，只需要根据学科id查询这个学科的详细信息。
    """
    @method_decorator(login_required)
    def get(self,request):
        #需要从GET请求中，获取要查询的学科的id。
        subject=Subject.objects.get(id=request.GET.get('subject_id'))
        #将这个学科对象，渲染到subject/detail.html中。
        return render(request,'subject/detail.html',locals())

class SubjectEditView(View):
    """
    渲染修改页面(GET),提交数据进行修改(POST)。
    """
    @method_decorator(login_required)
    @manage_promessions(template_name='subject/list.html', model_name='subject')
    def get(self,request, subject):
        """
        在登录用户点击 "编辑" 按钮的时候，需要先判断登录用户，所点击的这个学科的创建者是否是当前登录用户，如果当前学科的创建者和当前登录用户是同一个用户，就可以跳转到编辑页面；或者说当前登录用户是amdin管理员，也可以跳转到编辑页面。
        """
        #获取学科ID，根据ID查询学科详情，将所有的学科数据渲染到subject/edit.html中。
        # subject=Subject.objects.get(id=request.GET.get('subject_id'))
        # if request.user.username!=subject.creater.username and request.user.username!='admin':
        #     error={'code':'只能编写自己添加的学科。'}
        #     subjects=Subject.objects.all()
        #     return render(request,'subject/edit.html',locals())
        # else:
        return render(request,'subject/edit.html',locals())

        #如何根据admin管理员给用户分配权限，来实现相应的功能。
        #思路：通过判断当前登录用户，是否包含在学科对应的用户列表中(一个学科对应了多个用户，而这个用户就是可以编辑该学科的用户，也是拥有权限的用户)；如果当前登录用户在列表中，就拥有权限，反之就没有权限。
        # subject=Subject.objects.get(id=request.GET.get('subject_id'))
        # #根据subject获取对应的权限用户列表(根据从表数据查主表)
        # promession_users=subject.promession_users.all()
        # #获取用户名username放在promession_users列表中。
        # promession_users=[user.username for user in promession_users]
        # if request.user.username in promession_users:
        #     #如果在权限列表中:
        #     return render(request,'subject/edit.html',locals())
        # else:
        #     #不在权限列表中;
        #     error={'code':'对该学科没有权限'}
        #     subjects=Subject.objects.all()
        #     return render(request,'subject/list.html',locals())
    @method_decorator(login_required)
    def post(self,request):
        #先根据subject_id从数据库中获取老数据。
        subject=Subject.objects.get(id=request.GET.get('subject_id'))
        #获取表单输入的新数据。
        subject.name = request.POST.get('name')
        subject.days = request.POST.get('days')
        subject.amount = request.POST.get('amount')
        subject.number = request.POST.get('number')

        #在保存修改数据之前，先判断此次修改的学科名和学科列表中已经展示的学科名是否会重名。如果重名的话，不允许保存。
        result=Subject.objects.filter(name=subject.name)
        if result and result.first().id !=subject.id:
            #如果根据输入的subject.name名称查询到数据库中存在该学科，那么就判断查询出来的学科id和当前编辑的学科id是否相等，如果相等，说明学科名称没有修改；如果不相等，说明学科名称修改了。
            error={'code':'该学科名已经存在，不允许修改！'}
            return render(request,'subject/edit.html',locals())
        else:
            subject.save()
            return redirect(reverse('subject_list'))

class SubjectDeleteView(View):
    @method_decorator(login_required)
    @manage_promessions(template_name='subject/list.html', model_name='subject')
    def get(self,request,subject):
        subject.delete()
        return redirect(reverse('subject_list'))

#问题1:
#如何使用admin管理员，给普通用户分配学科权限。test1：python...
#问题二：
#如何利用装饰器，将
"""
如何利用装饰器，将
if request.user.username != subject.creater.username and request.user.username != 'admin':
    error = {'code': '只能删除自己管理的学科。'}
    subjects = Subject.objects.all()
    return render(request, 'subject/list.html', locals())
封装成装饰器，因为后续的二级页面，三级页面，四级页面都需要这样的权限判断。
"""
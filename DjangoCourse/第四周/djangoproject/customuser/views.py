from django.shortcuts import render,reverse,redirect
from django.contrib.auth import logout,login
from django.views.generic import View
from customuser.models import UserModels
from subject.models import Subject
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.http import HttpResponse
# Create your views here.
class UserLoginView(View):
    """
    处理用户登录注册的通用视图。
    """
    def get(self,request):
        return render(request,'user/login.html')
    def post(self,request):
        username=request.POST.get('account')
        password=request.POST.get('password')
        user=UserModels.objects.filter(username=username)
        if user:
            # check_password(password)：将输入的密码和数据库中该用户对应的密码进行验证，如果密码一致，返回True，密码不一致，返回False。
            # check_password()会对明文密码(输入框中输入的密码)进行加密，然后再和数据库中的密码进行对比。所以使用check_password()对密码进行验证，要求数据库中的密码必须是加密的。
            if user.first().check_password(password):
                login(request,user.first())
                return redirect(reverse('subject_list'))
            else:
                error={'code':'密码错误！'}
        else:
            error={'code':'用户名不正确！'}
        return render(request,'user/login.html',locals())
class UserLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('subject_list'))

# 定义一个装饰器，用于对用户的访问权限进行控制。
def manage_promessions(template_name, model_name):
    def promession(fun_name):
        def wrapper(self, request):
            if model_name=='subject':
                subject = Subject.objects.get(id=request.GET.get('subject_id'))
                """
                if request.user.username != subject.creater.username and request.user.username != 'admin':
                    error = {'code': '只能删除自己管理的学科。'}
                    subjects = Subject.objects.all()
                    return render(request, template_name, locals())
                else:
                    # 通过权限认证，要执行具体的业务逻辑。
                    # 把Django传给闭包函数wrapper的参数，继续传给被装饰函数def get(self, request):
                    result = fun_name(self, request, subject)
                    # def get(self, request)加上装饰器以后，函数内部的返回值HttpResponse不再直接返回给Django了，因为此时Django已经不会直接调用这个get函数，Django是在调用这个闭包函数。
                    return result
            """
                if request.user.roles==0 and request.user.username==subject.creater.username:
                    # 如果你是普通用户，并且这个普通用户也是所操作的这个学科的创建者，所以，是可以跳转到编辑页面的。
                    return fun_name(self,request,subject)
                elif request.user.roles == 1:
                    # 如果是黄金会员，除了可以修改自己添加的学科，还可以修改Python学科(这个学科是别的用户创建的)。
                    if request.user.username==subject.creater.username or subject.name=='Python':
                        return fun_name(self,request,subject)
                elif request.user.roles == 2:
                    # 超级会员，可以修改所有学科
                    return fun_name(self, request, subject)
                # 以上条件都不满足，说明权限不够。
                error = {'code': '没有权限操作该学科，如果需要，请充值！'}
                subjects = Subject.objects.all()
                return render(request, template_name, locals())
            elif model_name == 'stage':
                print('阶段')
            elif model_name == 'outline':
                print('阶段大纲')
            elif model_name == 'program':
                print('章节')
        return wrapper
    return promession

def headimg(request):
    if request.method == 'POST':
        # 前端ajax请求，将图片对象、图片名称传递到了后台的views.py中；
        img = request.FILES.get('img_file')
        # 获取数据库head_img字段的值，并切割成列表。
        # ['2018', '10', 'h2.png']
        path = request.user.head_img.url.split('/')
        # 将列表的最后一个元素图片名称，替换成新的图片名称
        path[-1] = request.POST.get('img_name')
        # 再将列表合成一个字符串
        path = '/'.join(path)

        url = settings.MEDIA_ROOT + '/' + path

        # 将ajax传过来的图片写入到本地/static/images/....目录下。
        with open(url, 'wb') as f:
            for chunk in img.chunks():
                f.write(chunk)

        # 以上步骤实现了图片的后台保存，还需要修改当前用户数据库中的头像路径。
        request.user.head_img = path
        request.user.save()

        return HttpResponse('图片上传成功')


def checkpwd(request):
    """
    检查原密码。
    :param request:
    :return:
    """
    pwd = request.GET.get('pwd')
    if request.user.check_password(pwd):
        return HttpResponse('Success')
    return HttpResponse('Error')


class UserUpdateView(View):
    """
    用户资料编辑页面。
    """
    def get(self,request):
        return render(request,'user/useredit.html')
    def post(self,request):
        nickname=request.POST.get('nickname','')
        if nickname:
            request.user.nickname=nickname
        mobile=request.POST.get('mobile','')
        if mobile:
            request.user.mobile=mobile
        address=request.POST.get('address','')
        if address:
            request.user.address=address
        sex=request.POST.get('sex','')
        if sex:
            request.user.sex=sex
        request.user.save()
        return render(request,'user/useredit.html')
class UserModifyView(View):
    """
    修改用户密码。
    """
    def get(self, request):
        return render(request, 'user/usermodify.html')

    def post(self, request):
        n_pwd = request.POST.get('n_pwd')
        c_n_pwd = request.POST.get('c_n_pwd')
        if n_pwd != c_n_pwd:
            return render(request, 'user/usermodify.html', {'error': "两次密码不一致"})
        else:
            # 两次密码一致，可以修改，修改成功以后，自动退出当前用户，使用新密码登录。
            request.user.password = make_password(n_pwd)
            request.user.save()
            logout(request)
            return redirect(reverse('user_login'))

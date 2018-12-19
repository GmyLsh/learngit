from django.shortcuts import render,HttpResponse,redirect
from .models import UserModels,EmailCodeModel
from .forms import RegisterForm,ForgetForm,ResetpwdForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout,login,authenticate
from utils.customemail import send_email_to_user
# 账户邮箱激活:
#当用户注册账号成功后，系统会默认向注册邮箱发送一封邮件，邮件包含一个账号激活链接，用户点击这个链接以后，此账号才被激活，才能够正常进行登录；如果用户没有点击激活链接，此账号是无法正常登陆的；

#账户找回密码:
#账户重置密码:
def index(request):
    return render(request,'index.html')
def register(request):
    if request.method=='GET':
        #创建验证码表单，渲染到模板展示验证码
        register_form=RegisterForm()
        return render(request,'register.html',{'register_form':register_form})
    elif request.method=='POST':
        # 实例化form，验证每个字段是否合法
        register_form=RegisterForm(request.POST)
        #判断register_form数据是否有效
        if register_form.is_valid():
            #cleaned_data 就是读取表单返回的值，返回类型为字典dict型
            email=register_form.cleaned_data['email']#读取name为'email'的表单提交值,并赋予email变量
            password=register_form.cleaned_data['password']
            #查询这个邮箱是否已经被注册过，如果已经被注册过了，返回错误信息；反之，则可以保存这个注册信息到数据库；
            if UserModels.objects.filter(email=email):
                return render(request,'register.html',{'register_form':register_form,'error':'邮箱已被占用！'})
            user=UserModels()
            user.email=email
            user.password=make_password(password)
            #把email的值存入UserModels中的username中
            user.username=email
            #用户注册成功，将is_active设置为0，等用户进行激活以后在将这个值改为1.
            #is_active:通常是指对象是否激活、启用、可用、正常状态。
            user.is_active=0
            user.save()
            #用户注册成功以后，需要激活之后才能登录。
            send_email_to_user(to_email=email,send_type='register')
            return render(request,'login.html',{'message':'激活邮件已发送至邮箱，请进行激活'})
        else:
            #如果数据无效，将含有错误信息的register_form再一次渲染到表单中。
            return render(request, 'register.html', {'register_form': register_form})


def active(request,code):
    """
    激活账户的函数
    :param request:
    :param code: 用户在邮件中，点击激活链接之后，后台会调用active()函数，同时会将激活码传给active()函数。
    :return:
    """
    if request.method=='GET':
        #对code进行验证
        try:
            email=request.GET.get('email','')
            email_record=EmailCodeModel.objects.get(code=code,send_type='register',email=email)
        except Exception as e:
            #code错误;
            return render(request,'active_fail.html')
        else:
            #code正确:将用户的is_active的状态修改为1；
            user=UserModels.objects.get(email=email_record.email)
            user.is_active=1
            user.save()
            return render(request,'login.html')


def login_func(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        email=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=email,password=password)
        if user:
            # user_obj=user[0]
            #check_password对原始密码进行检查
            #authenticate:对明文密码再使用make_password进行加密之后，再和数据库中的密码进行对比；
            #make_password():对同一个字符串进行加密，得到的结果也是不一样的；
            if user.check_password(password):
                #登录前判断用户是否激活
                if user.is_active:
                    login(request,user)# 登录可以显示用户
                    return render(request,'index.html')
                else:
                    #如果用户没有激活:
                    #1.激活链接失效/激活邮件发送失败，造成用户没有激活；重新发送一封激活邮件；
                    #2.用户没有点击激活链接，提示用户去邮箱中激活账号；
                    if not EmailCodeModel.objects.filter(email=email):
                        send_email_to_user(to_email=email,send_type='register')
                        return render(request, 'login.html', {'error': '该用户没有激活，激活邮件已发送至{}邮箱，请激活'.format(email)})
            else:
                return render(request, 'login.html', {'error': '用户名或密码错误'})
        else:
            return render(request,'login.html',{'error':'用户名或者密码错误'})

def forget(request):
    """
    找回密码的视图函数
    :param request:
    :return:
    """
    if request.method=='GET':
        forget_form=ForgetForm()
        return render(request, 'forget.html', {'forget_form': forget_form})
    elif request.method=='POST':
        #获取邮箱，验证邮箱是否存在，如果邮箱存在，向这个邮箱发送一个邮件，邮件中包含找回密码的连接。用户点击这个连接，会跳转到找回密码页面。
        forget_form=ForgetForm(request.POST)
        if forget_form.is_valid():
            #cleaned_data 就是读取表单返回的值，返回类型为字典dict型
            email=forget_form.cleaned_data['email']
            if UserModels.objects.filter(email=email):
                result=send_email_to_user(email,send_type='forget')
                if result:
                    return render(request,'send_email_sucess.html',{'email':email})
                else:
                    #邮件发送失败
                    forget_form=ForgetForm()
                    return render(request,'forget.html',{'forget':forget_form,'error':'邮件发送失败'})
            else:
                forget_form=ForgetForm()
                return render(request,'forget.html',{'forget':forget_form,'error':'该用户不存在'})
        else:
            return render(request, 'forget.html', {'forget': forget_form})
def reset_pwd(request,code):
    if request.method=='GET':
        records=EmailCodeModel.objects.filter(code=code,send_type='forget')
        if records:
            record=records[0]
            return render(request,'reset_pwd.html',{'email':record.email,'code':code})
        else:
            return render(request,'forget_fail.html')
    elif request.method=='POST':
        #重置密码
        reset_form=ResetpwdForm(request.POST)
        if reset_form.is_valid():
            #数据有效，验证两次密码是否一致
            email=request.POST['email']
            pwd=reset_form.cleaned_data['password']
            r_pwd=reset_form.cleaned_data['r_password']
            if pwd==r_pwd:
                #两次密码一致，可以修改，需要获取当前密码对应的用户。
                user=UserModels.objects.get(email=email)
                user.password=make_password(pwd)
                user.save()

                #用户重置密码成功之后，需要将当前用户的所有发送的找回密码的邮件记录删除。防止邮件记录表中保存过多的邮件记录。
                EmailCodeModel.objects.filter(email=email,send_type='forget').delete()
                logout(request)
                return redirect('/login/')
            else:
                return render(request,'reset_pwd.html',{'error':'两次密码不一致'})
        else:
            return render(request,'reset_pwd.html',{'error':'数据无效'})
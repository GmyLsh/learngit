from django.shortcuts import render,redirect
from django.contrib.auth.views import login_required
from django.views.generic import View
from django.utils.decorators import method_decorator
from .models import UserModel
from django.contrib.auth import login,logout
"""
需求:用户想要访问首页页面，必须先进行登录。如果用户在没有登录的前提下，直接就访问首页页面，那么页面要求自动跳转到的登录页面，等用户登陆成功以后，在跳转到首页。
"""


# Create your views here.
def login_fun(request):
    if request.method=='GET':
        return render(request, 'login.html')
    elif request.method=='POST':
        #需要验证用户名和密码
        username=request.POST.get('account')
        password=request.POST.get('password')
        #验证输入的用户名和密码，和数据库中保存的用户名和密码是否一致.
        #1.先根据username去数据库中查寻是否存在该用户名
        try:
            usermodel=UserModel.objects.get(username=username)
            if usermodel:
                #再判断密码是否一致
                if password==usermodel.password:
                    #说明用户名一致、密码一致,登陆成功，跳转到首页。
                    #Django中使用True或者False这两种状态，来表示当前用户是否登录成功。
                    #通过django内置的login函数，来修改当前用户的user的登录状态is_authenticated。
                    print('===',request.user.is_authenticated)#AnonymousUser(匿名用户，暂时不知道用户名。)
                    print('||||',request.user.is_authenticated)
                    login(request,usermodel)#比较是否正确
                    #request.user：是一个固定的组合，他表示：获取 发起此次请求的用户对象。并且这个对象指的是登陆成功以后的user对象。
                    print('....',request.user)
                    print('++',request.user.is_authenticated)
                    print('----')
                    #在用户没有登录之前，request.user的值是一个匿名用户，可以理解为当前这个请求是没有用户的
                    return redirect('/index/')

                else:
                    #说明用户名一致，密码和数据库中的密码不一致。
                    return render(request,'login.html',{'error':'用户名或者密码错误！'})
        except:
            return render(request, 'login.html', {'error': '用户名或者密码错误！'})




# @login_required这个是能用于视图函数上。

# @login_required
def index(request):
    return render(request, 'index.html')
# @method_decorator(login_required)用于通用视图类中的函数，哪一个函数需要进行登录，就在函数上添加这个装饰器即可
class Stu(View):
    @method_decorator(login_required)
    def get(self,request):
        print(request.user)
        return render(request,'index.html')
    def post(self):
        pass


def logout_fun(request):
    #内置函数,主要就是将request.user=AnonymousUser()设置成为了一个匿名用户，而匿名用户的is_authenticated的属性值就是False。
    logout(request)
    # return render(request,'index.html')
    #当用户退出以后，需要重定向到首页，如果你直接渲染首页的页面，只是页面发生了改变，地址栏中的地址和页面是不匹配的。所以，需要加载首页页面不再通过render()，而是通过重新向/index/地址发送一个请求来达到加载首页页面的目的。
    return redirect('/index/')
# render()和重定向的区别redirect()函数的区别:
#1.
#render()函数只渲染模版，可以向模板传递数据，但是render()函数不会再发送请求。
#redirect()函数只能重定向url，也就是这个函数的参数只能是url。这个函数的作用就是向这个url再发送一个GET请求。

#2.
#render()只是返回响应，不会改变地址栏中的地址:redirect()由于又发送了一次请求，所以，地址栏中的地址也会改变。

#区分如何使用：是否需要切换地址栏中的地址。




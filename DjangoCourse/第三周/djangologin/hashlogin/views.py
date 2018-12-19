from django.shortcuts import render,redirect
from django.views.generic import View
from django.contrib.auth import authenticate
from login.models import UserModel
from django.contrib.auth import login,logout
from .forms import LoginForm


class HashpassView(View):
    def get(self,request):
        return render(request,'login.html')

    # def post(self,request):
    #     username = request.POST.get('account')
    #     password = request.POST.get('password')
    #
    #     # 如果密码是加密的密码，需要使用Django的认证函数authenticate对账号密码进行认证。
    #     # authenticate认证原理：1.先根据用户名去数据库中查询是否存在该用户，如果存在该用户，再验证密码是否正确，如果密码也正确，再验证该账号的is_active是否被激活（True就是激活了），如果账号也被激活了，此时返回这个UserModel对象
    #     # 2.如果用户不存在，返回None；
    #     user = authenticate(username=username,password=password)
    #     if user:
    #         # 说明用户名和密码都是正确的。
    #         # 使用login()函数进行逻辑登录。
    #         login(request,user)
    #         # 登录成功以后，跳转到首页。
    #         return redirect('/index/')
    #     else:
    #         # 如果数据不正确，不需要跳转url地址，也不需要跳转页面，就需要再渲染一下页面，展示错误信息即可。
    #         return render(request,'login.html',{'error':'用户名或密码错误'})

    def post(self,request):
        #Html模板中自定义的<input>标签如何跟自定义表单结合使用
        #主要就是使用了Form表单的数据检查功能，不在html模板中使用{{form}}这种形式生成的input标签

        #注意:在自定义form表单中，表单属性必须和<input>标签中name属性的值保持一致。
        # 注意:在自定义form表单中，表单属性必须和<input>标签中name属性的值保持一致。
        # 注意:在自定义form表单中，表单属性必须和<input>标签中name属性的值保持一致。
        formdata=LoginForm(request.POST)
        if formdata.is_valid():
            username=formdata.cleaned_data['account']
            password=formdata.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user:
                login(request,user)
                return redirect('/index/')
            else:
                return render(request,'login.html',{'error':'用户名或密码不正确'})
        else:
            return render(request,'login.html',{'error':'数据不合法'})

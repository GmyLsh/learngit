from django.shortcuts import render,reverse,redirect,HttpResponseRedirect
from django.http import HttpResponse
"""
redirect()：返回值是HttpResponseRedirect类的对象。这个函数只能给前端返回一个Response，不能修改Response，比如响应头、响应状态等；
HttpResponse：只能返回一个文本内容的Response对象。该类是可以设置响应头的。
HttpResponseRedirect：该类既可以设置响应头，又有重定向的功能。
"""


from .models import UserModel

"""
django中的cookie和session：
1. 用户在前端登录以后，此时django会在django_session这个表中，生成一个键值对：session_key和session_data；其中，session_key是用于在响应中通过Set-Cookie字段返回给浏览器，浏览器会将这个session_key(sessionid)的值存储到本地；
2. 等用户登录完以后，在访问其它页面的时候，浏览器就会将这个本地cookie中的sessionid这个键的值，放在请求头中，交给后台django，django在接收到这个sessionid值的时候，会利用这个值向表django_session获取session_data的值，进而判断用户是否处于登录状态；
3. session_data的值是利用用户名+密码生成的一个加密字符串，这个字符串就是用来表明用户的登录状态，如果用户登录成功，那么django_session就会生成一个session_data；用户没有登录成功，是不会有session_data数据的。

session的过期时间：django默认设置是2周。如果session过期，浏览器再携带之前的cookie就不能免登录了，因为cookie已经失效了。
前端：如果超出了session的过期时间，那么浏览器会自动将对应的cookie删除掉；
后端：django没有对过期的session做任何处理；

如何删除后台保存的一些过期的session信息：
执行命令：python manage.py clearsessions

如果用户在过期时间内主动退出登录，那么django会将该用户对应的session数据给删除掉(request.session.flush())。
但是如果用户在登录完以后没有主动退出，并且超出了过期时间，用户需要重新登录，但是django中的过期session是不会被清理的。需要定期清理过期的session数据。
"""

"""
用户的登录两种方式：
1. 使用login()和logout()这两个内置函数实现登录和退出；缺点就是用户的登录是在操作同一个request.user，导致同一台电脑不能同时登录两个用户；
2. 如果同一台电脑的同一个网站，登录多个账号，为了防止串号，不能再使用login()和logout()函数了，可以通过session和cookie来实现这个需求；
"""


def login_fun(request):
    if request.method == 'GET':
        # 每次在登录的时候，都要去cookie中获取username的值。
        name = request.COOKIES.get('username', '')
        return render(request, 'login.html', {'name': name})
    elif request.method == 'POST':
        uname = request.POST.get('username')
        upassword = request.POST.get('password')
        user = UserModel.objects.filter(uname=uname, upassword=upassword)
        if user:
            # 用户名密码都正确。
            # 需要判断用户是否勾选了 "记住用户名"，如果勾选了，可以将这个用户名保存到浏览器的cookie中，并且可以设置过期时间。cookie一旦被浏览器缓存，除非cookie过期了，cookie不会受到项目的是否运行的影响。
            is_jizhu = request.POST.get('box')
            response = HttpResponseRedirect('/index/')
            if is_jizhu:
                # 用户选择了记住，后台如何向前端传递cookie? 响应头中的Set-Cookie
                response.set_cookie('username', uname)

            else:
                # 如果用户没有勾选记住。将username这个cookie置为空。
                response.set_cookie('username', max_age=1900000)

            # 在向浏览器返回cookie的同时，也需要向后台表django_session中添加用户的登录状态session_data.
            request.session['username'] = uname

            return response
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})


def index(request):
    return render(request, 'index.html')

def logout_fun(request):
    # 如果用户退出，需要将登录时生成的session信息删除，等用户再次登录的时候，需要重新生成session.
    request.session.flush()
    return redirect('/index/')
def register(request):
    if request.method=='POST':
        if request.is_ajax():
            #is_ajax()这个方法是用于区分这个POST请求是否是ajax发送的POST请求。因为form表单也能发送POST请求。
            name=request.POST.get('username')
            pwd = request.POST.get('password')
            user=UserModel(uname=name,upassword=pwd)
            user.save()
            return HttpResponseRedirect('ok')

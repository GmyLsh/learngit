from django.http import HttpResponseRedirect
def islogin(func):
    def login_fun(request, *args, **kwargs):
        if request.session.get('username'):
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            #假如要进入用户中心但没有登录者黑就记录用户中心的url并传给set_cookie，并返回到登录页面，登录完成后直接跳转到用户中心
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun

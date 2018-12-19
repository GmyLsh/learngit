"""
座右铭:将来的你一定会感激现在拼命的自己
@project:DjangoCourse
@author:Mr.Zhang
@file:urls.PY
@ide:PyCharm
@time:2018-10-17 09:35:07
"""
"""
url.py文件中的这些path地址，称为url路由，就是url地址。
如何通过url路由，向视图函数(Function views)传递参数
"""
from django.urls import path,re_path
from urlparams import views
urlpatterns =[
    #1.直接在浏览器的url后，使用?和&符号拼接参数，视图函数应如何接受参数？
    path('args/',views.params_firse),
    # 2.参数不在以?的形式进行拼接，而是以路径的形式/a/a/a/的形式传递的，视图函数应该如何接收参数？
    #/(\d+)(\w+)/就是给视图函数传递的两个参数。
    #视图函数想要接收，在函数中必须声明两个形参(形参的名称可以任意设定)来接受这两个参数。
    # re_path(r'^params/(\d+)/(\w+)/$',views.params),
    re_path(r'^params/(\d{2})/(\w+)/$',views.params),
    #将re_path转化成path()的写法：
    #视图函数接受参数，params1必须声明两个形参(形参的名称必须和路由中指定的参数名称保持一致)。
    #<>是用来匹配参数的。
    #<>中的参数是可以指定转换器的，转换器的作用就是对拦截的参数进行参数转换，比如类型转换，值的转换等。
    #默认转化器是str
    path('params1/<str:username>/<int:password>/',views.params1),
    #3.path()函数除了上述将参数直接以路径的形式传递给视图函数，也可以采用如下方法传递参数。
    #params2()需要设置形参，形参的名称和字典的键保持一致。
    path('params2/',views.params2,{'user':'陈罗文','pwd':'25'}),
    #4.re_path()这种url路由，如何指定参数的名称。而上面的re_path中，参数的名称可以任意设定。
    #?P:是一种固定的语法格式。
    #<id>、<username>就是形参的名称，此时是视图函数params3()的形参必须和id、username保持一致。
    #<id>/d+:表示将\d+匹配到的数字参数，赋值给形参id。
    #<username>\w+:表示将\w+匹配到的字符参数，赋值给形参username。
    re_path(r'^params3/(?P<id>\d+)/(?P<username>\w+)/$',views.params3)
]
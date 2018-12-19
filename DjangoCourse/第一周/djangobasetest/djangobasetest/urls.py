"""djangobasetest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
#引入views.py中的函数(视图函数)
from base import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #一个url对应一个views.py中的函数。
    #创建url规则的几种方式:
    #第一种:path(URL地址，绑定的函数)
    path('index/',views.index),
    #第二种:re_path(url地址,绑定的视图函数)
    # django2.0之前的写法:url('^index/(name)/$',),之前的正则表达式写法过于复杂，所以通过path()进行了简化。
    # ^:表示这个url以....开头。 以...开始:^= , 以...结尾：$=  包含:*=
    # $:这个url以...字符结尾
    re_path(r'^one/$',views.index),

    #第三种:如果项目中含有多个app，每个app需要设置的url也很多，此时将所有url都写在同一个urls.py中就不行了，会让这个url看起来很乱，很多，不方便代码的调试。此时就需要将每个模块(app应用)的url放在每个模块的内部。
    #由于这个urls.py是在创建项目的时候生成的，所以这个文件是所有url的总入口，不管url是在哪一个设置的，最终都要在这个总入口的urls.py文件中进行配置。
    #base/这个地址映射的是base.urls中的url。
    path('base/',include('base.urls')),
    #base1/这个地址映射的是base1.urls中的url。
    path('base1/',include('base1.urls')),
    #base2/这个地址映射的是base2.urls中的url。
    path('base2/',include('base2.urls')),

    #入口地址(可以省略：base/)+模块地址=完整地址
]

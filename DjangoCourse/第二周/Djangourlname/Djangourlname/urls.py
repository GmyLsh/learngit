"""Djangourlname URL Configuration

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
from django.urls import path,re_path
from urlname import views

#name参数的作用：主要是通过name的值，来查找url地址，可以理解为反射的作用。在html模板中使用name来反射url，优势就是后期url规则发生改变之后，只需要吊证urls.py即可，所有的模板文件都不需要修改
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_sum/',views.add,name="add"),
    re_path(r'^add/(\d+)/(\d+)/$',views.add1,name="add1"),
    path('get_url/',views.get_url,name="test"),
    path('index/',views.index)
]

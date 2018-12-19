"""movie URL Configuration

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
from django.urls import path
from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
]
#数据库：一对一、一对多、多对多。
#Django的admin后台管理
#Django的登录注册

#小项目：
#项目：

#Django的用户激活和密码找回。
#Django的cookie和session。
#Django的restful接口。
#项目：

#Django的前后端分离技术
#Vue.js

#项目：restful+vue

# Django的前后端分离：restfulframework这个包
#项目：restfulframework+vue

#Django的线上(服务器)部署
#Django的负载均衡和反向代理。(Linux常用文件和常用命令)

# 面试问服务器的知识：运维
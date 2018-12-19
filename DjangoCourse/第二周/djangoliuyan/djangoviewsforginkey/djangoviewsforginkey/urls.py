"""djangoviewsforginkey URL Configuration

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
from viewsforginkey.views import Home,DataHandler
from django.views.generic import TemplateView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/<id>/',Home.as_view(),name="index"),
    #TemplateView:如果一个通用视图类只处理GET请求不处理POST请求，那么可以使用TemplateView这个类，这个类只需要配置url路由即可。
    path('index1/',TemplateView.as_view(template_name='index.html'),name="index1"),
    path('index/',DataHandler.as_view(),name="handler")
]

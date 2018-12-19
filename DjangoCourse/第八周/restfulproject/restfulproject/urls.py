"""restfulproject URL Configuration

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
from django.urls import path, re_path, include
from apitest.views import StudentView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',StudentView.as_view()),
    #这个接口是drf提供的用于在调式接口时进行登录和退出的。
    re_path(r'^api-auth/', include('rest_framework.urls')),
    # #设置用户认证API接口。
    # path('api/v1/auth/',AuthView.as_view()),
    # #商品列表页的API接口
    # path('api/v1/order/',OrderView.as_view()),
    # path('api/v1/detail/',OrderDetailView.as_view()),

    #http://localhost:8000/api/order/
    # path('api/',include('apitest.urls')),
    path('api/<str:version>/',include('apitest.urls'))
]

"""djangoshengxian URL Configuration

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
from shengxian.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',register),
    path('index/',index),
    path('login/',login_fun),
    path('logout/',logout_out),
    path('list/',list_page,name='list'),
    path('detail/',detail,name='detail'),
    path('cart/',cart),
    path('place_order/',place_order),
    path('shop_cart/',shop_cart,name='shop_cart'),
    path('user_center_info/',user_center_info),
    path('user_center_order/',user_center_order),
    path('user_center_site/',user_center_site),
]

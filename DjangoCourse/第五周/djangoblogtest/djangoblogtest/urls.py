"""djangoblogtest URL Configuration

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
from django.views.static import serve
from django.conf import settings
from blog.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    #/uploads/2018/11/1.jpg
    #/uploads/2018/10/1.jpg
    #关联自定义的上传图片的路径
    re_path(r'uploads/(.*)$',serve,{'document_root':settings.MEDIA_ROOT}),
    path('admin/upload/',upload_img),
    path('index/',index),
    path('archive/<str:year>/<str:month>/',archive)
]
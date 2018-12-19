"""
座右铭:将来的你一定会感激现在拼命的自己
@project:djangozuoye
@author:Mr.Zhang
@file:urls.PY
@ide:PyCharm
@time:2018-10-24 19:21:03
"""
from liuyan import views
from django.urls import path

urlpatterns = [
    path('index/', views.index,name="index"),
    path('add/', views.add,name="add"),
    path('update/', views.update,name="update"),
]
"""
座右铭:将来的你一定会感激现在拼命的自己
@project:DjangoCourse
@author:Mr.Zhang
@file:urls.py.PY
@ide:PyCharm
@time:2018-10-16 17:15:37
"""
"""
写base这个模块的所有的url地址
"""
from base import views
from django.urls import path,re_path
#开始配置base这个app应用，所对应的url地址。
urlpatterns=[
    path('index/',views.base_index),
    path('list/',views.base_list),
]
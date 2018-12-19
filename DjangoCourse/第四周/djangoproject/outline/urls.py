"""
座右铭:将来的你一定会感激现在拼命的自己
@project:djangoproject
@author:Mr.Zhang
@file:urls.PY
@ide:PyCharm
@time:2018-11-02 21:03:01
"""
from django.urls import path
from .views import *
urlpatterns = [
    path('list/',OutlineListView.as_view(),name='ol_list'),
    path('add/',OutlineAddView.as_view(),name='ol_add')
]
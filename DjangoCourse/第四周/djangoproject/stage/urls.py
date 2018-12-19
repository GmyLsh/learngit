"""
座右铭:将来的你一定会感激现在拼命的自己
@project:djangoproject
@author:Mr.Zhang
@file:urls.PY
@ide:PyCharm
@time:2018-11-02 21:03:21
"""
from django.urls import path
from .views import *
urlpatterns = [
    path('list/', StageListView.as_view(),bane='stage_list'),
    path('add/',StageAddView.as_view(),name='stage_add')
]
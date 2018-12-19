from django.urls import path,re_path,include
from .views import *
urlpatterns = [
    #设置用户认证API接口。
    path('auth/',AuthView.as_view()),
    #商品列表页的API接口
    path('order/',OrderView.as_view(),name='order'),
    #商品详情页API
    path('detail/',OrderDetailView.as_view()),
    # serializer的接口
    path('roles/',RoleView.as_view()),
    path('users/',UserView.as_view()),
    path('groups/',GroupView.as_view()),
    path('valication/',ValicationView.as_view()),
    path('pagination/',PaginationView.as_view()),
    path('gen/',GenericView.as_view()),
    #get 对应两个参数1.list获取所有参数 2.retrieve获取一个参数
    path('genviewset/<int:pk>/',GenericViewSetView.as_view({'get':'retrieve'})),
]
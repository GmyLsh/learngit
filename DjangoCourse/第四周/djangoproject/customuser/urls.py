from django.urls import path
from .views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/',UserLogoutView.as_view(),name='user_logout'),
    path('info/',TemplateView.as_view(template_name='user/userinfo.html'),name='user_info'),
    path('headimg/',headimg,name='user_img'),
    path('checkpwd/', checkpwd, name='user_check_pwd'),
    path('update/', UserUpdateView.as_view(), name='user_update'),
    path('updatepwd/', UserModifyView.as_view(), name='user_update_pwd'),

]
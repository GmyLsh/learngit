from django.contrib import admin
from .models import *
# Register your models here.
#只要使用admin后台系统，所有的Model必须在这里进行注册，否则，admin后台是不会显示相关Model的
admin.site.register(UserModel)
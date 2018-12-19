from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(FoodType)
admin.site.register(FoodProduct)
admin.site.register(UserModels)
admin.site.register(UserInfo)
admin.site.register(ShopDetail)
admin.site.register(ShopCart)
admin.site.register(Order)
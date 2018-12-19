from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
   list_display = ('title','desc','click_num','comment_num')

   #设置admin后台文章Model列表页，那些字段可以被点击。
   list_display_links = ('title','desc')

   #设置哪些字段可以被编辑
   # list_editable = ('click_num','comment_num')

   #设置添加文章时，显示哪些字段。
   # fields = ()

   #由于文章添加需要使用副文本编辑器，所以在这里，指定副文本编辑器要使用的一些css、js等文件;
   class Media:
       js=(
           '/static/kindeditor/kindeditor-all-min.js',
           '/static/kindeditor/lang/zh-CN.js',
           '/static/kindeditor/config.js',
       )



admin.site.register(UserModel)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Comment)
from django.contrib import admin

# Register your models here.
# 将models.py中的所有的model类都要在这里进行注册，如果你的项目没有使用admin，这里是不需要注册的。只有使用admin，才需要在这里注册。
from .models import *


# 这种注册方式，默认只在admin站点的文章列表页中，显示一个字段。
# admin.site.register(Article)

# 如果需要在admin站点中的文章列表页中，显示多个字段，需要下面这种写法。
class ArticleAdmin(admin.ModelAdmin):
    # list_display这个属性就是用于定义文章列表页显示哪些字段，列表中的值，必须要和model类中声明的字段保持一致。
    list_display = ['a_title', 'a_author', 'a_publish_date']
    # 这个fields字段作用于Model的添加页面，显示哪些字段可以用于输入内容，不在列表中的数据，默认添加页面就不在显示了。
    # fields=['a_title']
    # fields属性和fieldsets属性不能同时使用。因为都作用于添加页面
    fieldsets = [
        ('标题信息', {'fields': ['a_title']}),
        ('作者信息', {'fields': ['a_author'], 'classes': ['collapse']}), ]
    # 针对文章列表页的一个属性配置，在列表页的右侧会出现一个过滤器，可以根据文章的发布时间或者作者对列表页的文章进行筛选。
    list_filter = ['a_publish_date', 'a_author']
    # 在文章的列表页顶部会出现一个搜索框。只能根据search_fields内定义的字段值进行搜索。

    search_fields = ['a_publish_date', 'a_author']


admin.site.register(Article, ArticleAdmin)

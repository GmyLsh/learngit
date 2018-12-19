"""
座右铭:将来的你一定会感激现在拼命的自己
@project:DjangoCourse
@author:Mr.Zhang
@file:customtags.PY
@ide:PyCharm
@time:2018-10-18 10:16:56
"""
from django import template

#1.先创建一个过滤器注册器，用于注册自定义的过滤器。
register=template.Library()
#2.可以自定义过滤器,只需要携带这个装饰器@register，就可以实现注册了。
@register.filter
def filter_chars(value,arg):
    print('----',arg)
    """
    该过滤器可以实现对字符串的切片功能。多余字符串省略。
    :param value:这个值是视图函数给模板传递的原始数据。
    :return:就是处理之后的数据。
    """
    return value[0:arg]+'...'
#3.自定义html标签
import datetime
#simple_tag这种类型的标签不能使用过滤器
@register.simple_tag
def html_tag(str,str1):
    print('====',str,str1)
    if str=="input":
        return '<input type="text" name="username" placeholder="输入密码"></input>'
    return '<p>自定义的p标签'

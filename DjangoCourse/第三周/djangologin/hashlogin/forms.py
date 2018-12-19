"""
座右铭:将来的你一定会感激现在拼命的自己
@project:djangologin
@author:Mr.Zhang
@file:forms.PY
@ide:PyCharm
@time:2018-10-31 14:12:35
"""
from django import forms
class LoginForm(forms.Form):
    account=forms.CharField(required=True)
    password=forms.CharField(required=True)
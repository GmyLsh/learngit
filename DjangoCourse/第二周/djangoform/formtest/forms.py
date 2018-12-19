"""
在这个文件中可以实现form表单的定制。
form.py文件名是固定的，不能修改。
"""
from django import forms

#1.先声明一个form类
class CustomForm(forms.Form):
    #2.定制两个input标签，用于输入a和b的值。
    #IntegerField()用来表明输入框值的类型。
    #label参数对应的就是<label for="a">数字a:</label>
    #widget表示控件，input就是一个控件。如果默认控件提供的功能不够用，那么可以重新定制控件。比如input控件默认没有显示placeholder。
    #xxxField()和xxxInput()两者进行区分
    #xxxField()决定了输入框中能输入的数据类型。
    #而xxxInput()一般和xxxField()是对应的，它xxxInput()一般是用来重写控件属性的。决定了控件的样式。
    a=forms.IntegerField(label='数字A',widget=forms.NumberInput(attrs={'placeholder':'请输入数字','class':'number'}),max_value=10,error_messages={'invalid':'数据超出长度'})

    #required表示该输入框的值是否是必须要填写的，默认为True。
    b=forms.IntegerField(label='数字B',required=False)
#3.在views.py中使用这个CustomForm类渲染表单。
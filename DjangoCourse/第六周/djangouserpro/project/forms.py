from django import forms
from captcha.fields import CaptchaField
class RegisterForm(forms.Form):
    #验证代码来保证它们的值是有效的E-mail地址
    #required:属性规定必需在提交之前填写输入字段。
    #error_messages:字段填写不正确 会提示字典中的内容。
    email=forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})
    password=forms.CharField(required=True,min_length=6,error_messages={'invalid':'密码长度至少6位'})
    #配置验证码表单
    captcha=CaptchaField(error_messages={'invalid':'验证码错误'})

class ForgetForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '邮箱格式不正确'})
    # 配置验证码表单
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})

class ResetpwdForm(forms.Form):
    password=forms.CharField(min_length=6)
    r_password=forms.CharField(min_length=6)

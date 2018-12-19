from django.shortcuts import render
from django.core.mail import send_mail,send_mass_mail
from djangoemailtest.settings import EMAIL_HOST_USER,EMAIL_HOST_PASSWORD
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
# Create your views here.
def sendoneemail(request):
    """
    发送一封邮件
    参数依次是：
    邮件标题、邮件内容、发送者、接受者、授权用户、授权密码
    :param request:
    :return:返回邮件发送成功的个数
    """
    result=send_mail('Django测试邮件','这是一个测试邮件，由<%s>发送！'%EMAIL_HOST_USER,EMAIL_HOST_USER,['2838875177@qq.com','469192981@qq.com'],auth_user=EMAIL_HOST_USER,auth_password=EMAIL_HOST_PASSWORD)
    if result==1:
        return HttpResponse('一封邮件发送成功')
    else:
        return HttpResponse('一封邮件发送失败')

def sendmoreemail(request):
    """
    发送多封邮件
    :param request:
    :return:
    """
    message_one=('邮箱激活账户','这是您的邮箱激活码:xxx,点击激活',EMAIL_HOST_USER,[EMAIL_HOST_USER])
    message_two = ('账户密码找回', '这是您的账户密码:xxx,点击找回', EMAIL_HOST_USER, [EMAIL_HOST_USER])
    result=send_mass_mail((message_one,message_two))
    if result==2:
        return HttpResponse('多封邮件发送成功!!')
    else:
        return HttpResponse('多封邮件发送失败!!')
def sendhtmlemail(request):
    """
    发送带有html标签的邮件
    :param request:
    :return:
    """
    result=send_mail('一个链接','请点击以下链接:',EMAIL_HOST_USER,[EMAIL_HOST_USER],html_message='<a herf="https://www.baidu.com">https://www.baidu.com</a>')
    if result==1:
        return HttpResponse('HTML邮件发送成功')
    else:
        return HttpResponse('HTML邮件发送失败')
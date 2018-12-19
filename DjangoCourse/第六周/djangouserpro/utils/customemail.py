from project.models import EmailCodeModel
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
import random
def random_code(code_length=16):
    """
    该函数用于生成随机激活码，默认激活码长度是16位
    :param code_length:
    :return:
    """
    chars='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    #获取字符串长度
    chars_length=len(chars)-1
    #根据字符串的总长度，以及code_length，从chars中随机取出16位字符，再拼接成字符串就是激活码。
    code=''
    for x in range(code_length):
        #生成[0,chars_length]范围的随机整数再chars中取出对应的生成随机整数索引的字符
        code+=chars[random.randint(0,chars_length)]
    return code

#定义发送邮件的函数。
def send_email_to_user(to_email,send_type):
    """
    发送邮件
    :param to_email: 目的地邮箱
    :param send_type: 邮件发送类型(激活、忘记密码)
    :return:
    """
    #每发送一封邮件，都会在邮件记录表中生成一条邮件发送记录。
    code=random_code()
    email_recoder=EmailCodeModel()
    email_recoder.code=code
    email_recoder.email=to_email
    email_recoder.send_type=send_type
    email_recoder.save()
    if send_type=='register':
        email_title='注册激活邮件'
        email_body='<i>点击以下链接激活账户</i><a href="http://localhost:8000/active/%s/?email=%s">http://localhost:8000/active/%s/?email=%s</a>'%(code,to_email,code,to_email)
        #邮件的主题、内容、发送者、接受者
        #EmailMultiAlternatives类，他是EmailMessage的子类，他有一个方法attach_alternative() ，可以让邮件中包括多种形式的内容
        message=EmailMultiAlternatives(email_title,email_body,settings.EMAIL_SERNER,[to_email])
        #指定邮件类型
        message.content_subtype='html'
        #发送成功:result=1;反之，result=0;
        result=message.send()
        return result
    elif send_type=='forget':
        email_title = '重置密码邮件'
        email_body = '<i>点击以下链接重置密码</i><a href="http://127.0.0.1:8000/reset_pwd/%s/">http://127.0.0.1:8000/reset_pwd/%s/</a>' % (code,code,)
        message = EmailMultiAlternatives(email_title, email_body, settings.EMAIL_SERNER, [to_email])
        # 指定邮件类型
        message.content_subtype = 'html'
        # 发送成功:result=1;反之，result=0;
        result = message.send()
        return result
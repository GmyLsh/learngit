"""
公共的用户认证模块，单独方法公共的包utils中
"""
from apitest.models import UserToken
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from rest_framework.permissions import BasePermission
from rest_framework.throttling import SimpleRateThrottle

class Authentication(BaseAuthentication):
    """
    自定义的用户认证
    """
    def authenticate(self,request):
        token=request.GET.get('token')
        if not token:
            raise exceptions.AuthenticationFailed('没有携带token')
        else:
            token_obj=UserToken.objects.filter(token=token)
            if not token_obj:
                raise exceptions.AuthenticationFailed('token认证失败')
            else:
                return (token_obj[0].user, token_obj[0].token)

    def authenticate_header(self, request):
        """
        Return a string to be used as the value of the `WWW-Authenticate`
        header in a `401 Unauthenticated` response, or `None` if the
        authentication scheme should return `403 Permission Denied` responses.
        """
        pass

class PTPermission(BasePermission):
    message='对不起，你不是普通用户，无权限访问'
    """
    给普通用户设置拥有权限，VIP及以上用户没有权限，在使用的时候，哪一个接口符合这个需求，就可以将这个权限认证类添加上。
    """
    def has_permission(self,request,view):
        #首先要获取当前登录的用户
        user=request.user
        if user.user_type==1:
            #普通用户
            return True
        #如果是VIP及以上的用户没有权限
        return False


class VIPPermission(BasePermission):
    message='对不起你不是VIP，无权访问'
    """
    给VIP用户设置拥有权限，VIP及以上用户有权限，在使用的时候，哪一个接口符合这个需求，就可以将这个权限认证类添加上。
    """
    def has_permission(self,request,view):
        #首先要获取当前登录的用户
        user=request.user
        if user.user_type!=1:
            #VIP及以上用户
            return True
        #如果是普通用户没有权限
        return False

# class ThrottleAuth(BaseThrottle):
#     # 声明一个字典，用于保存不同用户的访问时间
#     visit_dict = {}
#     def __init__(self):
#         #visit_historys用来记录用户每次的访问时间的变量
#         self.visit_historys=[]
#     def allow_request(self, request, view):
#        """
#        认证用户是否能够向这个API接口发起请求。返回值是True，就可以访问；反之，就不能访问；
#        :param request:
#        :param view:
#        :return:
#        """
#        # 1.先从请求中获取对方IP地址；
#        # 固定用法
#        IP = request.META.get('REMOTE_ADDR')
#        # 2.获取当前用户向API接口发送请求的时间
#        current_time = time.time()
#        if IP not in self.visit_dict:
#             # 3.如果获取的当前IP，在self.visit_dict字典中不存在，说明这个IP地址是第一次访问。
#             self.visit_dict[IP]=[current_time]
#             #此时返回Ture，访问次数不够，可以继续访问
#             return True
#         #4.如果这一次的IP在记录里面已经存在了，说明不是第一次访问，和第一次访问的时间进行对比。
#        #获取IP对应的时间列表
#        history=self.visit_dict.get(IP)
#        self.visit_historys=history
#        while history and history[-1] < current_time - 60:
#            #当前时间-60s大于第一次访问的时间，说明这一次的访问和上一次的访问时间不在1分钟之内。
#            #将列表中的[-1]对应的数据删除
#            history.pop()
#         #5.经过上述循环之后，列表中剩余的就是1分钟之内的时间了。
#        if len(history) < 5:
#             #可以访问，1分钟之内没有访问超过5次。
#             history.insert(0,current_time)
#             return True
#         #6.当前访问总次数 >= 5次，不能在访问这个接口了。
#        return False


class IPThrottle(SimpleRateThrottle):
    """
    对匿名用户的控制
    使用throttling.py中的内置的访问控制类来实现API的访问控制
    """
    scope = 'IP'
    def get_cache_key(self, request, view):
        return request.META.get('REMOTE_ADDR')

class UserThrottle(SimpleRateThrottle):
    """
    对于已登录的用户的控制
    使用throttling.py中的内置的访问控制类来实现API的访问控制
    """
    scope = 'USER'
    def get_cache_key(self, request, view):
        return request.user.username
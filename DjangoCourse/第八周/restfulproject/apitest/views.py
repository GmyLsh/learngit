from django.http import JsonResponse
#APIView是drf中最基础的一个类，最底层的一个类，这个类继承于django的View类。
from rest_framework.views import APIView
from rest_framework.response import Response

from django.views import View
# from .models import UserInfo, UserToken
import hashlib, time

# Create your views here.

def md5(username):
    now=str(time.time())
    #利用用户名和时间戳进行Md5加密，返回一个随机字符串。
    md5_obj=hashlib.md5(bytes(username,encoding='utf8'))
    md5_obj.update(bytes(now,encoding='utf8'))
    return md5_obj.hexdigest()

"""
djangorestframework框架
1.这个框架是在django框架的基础上延伸出的一个框架，djangorestframework这个框架内部也应用了很多django的内容
2.这个框架提供了Web Browser API的接口调试页面；
3.这个框架提供了接口文档生成的方式，能够快速生成接口文档供前端使用；
4.提供了解析器，主要是ORM对象序列化成JSON，同时支持对数据的验证(格式的验证、正确性的验证);

"""
class StudentView(View):
    def get(self,request):
        return JsonResponse({'message':'GET请求发送成功'})

    def post(self,request):
        return JsonResponse({'message':'POST请求发送成功'})

    def put(self,request):
        return JsonResponse({'message':'PUT请求发送成功'})

    def delete(self,request):
        return JsonResponse({'message':'DELETE请求发送成功'})

#drf的认证组件的使用
#Authentication:这个认证主要就是对用户的登录状态进行判断，如果登陆了，认证成功：反之就认证失败。
#Permissions:权限，表示用户在认证成功(登录)的前提下，对一些接口是否拥有访问权限，有权限就可以访问，没有权限就不能访问.

#认证逻辑:当前端发送认证请求时，如果所产地的用户名和密码正确，此时，后台接口会给前端返回一个token值，以后只要请求中含有这个token值，后台就认为该用户已经登录了。

#throttling:访问控制认证，可以规定这个API接口在一个时间段内访问频率，适当减少服务器的压力。

#API接口版本的使用
#1./order/?version=v1/v2 将版本号携带在GET请求中(用的比较少)
#2. /api/v1/order/ 将版本写在路径中(最常用的方式)
#{'a':1} {'a':[{'x':1}]}
#3. Content-Type:application/json;version=v1 将版本号写在请求头中
#版本的作用：用于后台获取这接口的版本号，根据版本号的不同返回不同的数据。


#serializer序列化(重点是前两个)
#1.主要是序列化数据，将ORM对象序列化成json字符串。
#2.对前端提交一些数据可以进行验证，符合规则继续往下。
#3.可以在响应的json中生成url。

#分页pagination组件：?page=1&size=3组合和?limit=10&offset=1组合 offset偏移量，从当前偏移量开始展示 limit:每页展示几条数据，若不够，有几条展示几条

#重点
#1.需要知道APIView中，request请求对象由Django内置的WSGIRequest对象，转化成了新的Request对象(rest_framework.request.Request),这个新的类对原有的类进行的功能丰富。

class AuthView(APIView):
    #使用这个局部认证配置覆盖全局的认证配置。值为[]，表示不进行认证。
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    """
    用户认证接口
    """
    def post(self,request):
        """
        模拟用户的登录请求
        :param request:
        :return:
        """
        data={
            'code':1000,
            'status':1,
            'error':0,
        }
        try:
            username=request.data.get('username')
            password=request.data.get('password')
            results=UserInfo.objects.filter(username=username,password=password)
            if results:
                #用户传递的用户名和密码是正确的，此时给用户返回token，用户在发生接下来的请求时必须携带这个token，然后后台会对这个token进行认证，如果认证成功(request.user,request.auth赋值)，如果认证失败(request.user,request.auth的值返回为None)。
                #创建token值，给用户返回过去。
                token=md5(username)
                #首先要将这个token在数据库中保留一份，将来用于和用户上传的token值进行对比
                # update_or_create：如果用户没有token就创建一个，如果用户有token就更新替换
                UserToken.objects.update_or_create(user=results[0],defaults={'token':token})
                data['token']=token
            else:
                data['error']=1
                data['status']=0
                data['message']='用户名或者密码错误'
        except:
            data['error']=1
            data['status']=0
            data['message']='异常'
        return JsonResponse(data)
ORDER_DICT = {
    1:{
        'name':'鞋子',
        'price': 20,
        'color': 'red',
        'detail': '...',
        'type': '普通'
    },
    2:{
        'name':'风扇',
        'price': 20,
        'color': 'black',
        'detail': '...',
        'type': '普通'
    },
}

# from rest_framework.throttling import BaseThrottle
# import time

# from utils.base_authenticate import ThrottleAuth
from utils.base_authenticate import UserThrottle
# from utils.version import Version
from rest_framework.versioning import QueryParameterVersioning, URLPathVersioning
class OrderView(APIView):
    #认证token,局部配置认证
    # authentication_classes = [Authentication]
    authentication_classes = []
    permission_classes = []
    # versioning_class = Version
    #QueryParameterVersioning:通过?version=1来获取版本号的，和自定义的Version类功能差不多，但是QueryParameterVersioning提供了一些额外的配置在REST_FRAMEWORK
    # versioning_class = QueryParameterVersioning
    versioning_class = URLPathVersioning
    # throttle_classes = [ThrottleAuth]
    # permission_classes = [PTPermission]
    """
    用户认证:商品列表页接口，要访问这个API接口，必须是认证用户(登陆成功后的用户)，如果没有认证，则不允许访问这个接口。
    用户权限认证:QQ空间(普通用户就可以访问，前提需要登录)
    """
    def get(self,request,version):
        data={}
        # #首先验证用户传递的token值和数据库中的是否一致
        # token=request.GET.get('token')
        # data={}
        # if not token:
        #     data['status']=0
        #     data['message']='This User Not Auth.'
        #     return JsonResponse(data)
        # else:
        #     token_obj=UserToken.objects.filter(token=token)
        #     if not token_obj:
        #         data['status'] = 0
        #         data['message'] = 'This User Not Error.'
        #         return JsonResponse(data)
        #     else:
        #         data['results']=ORDER_DICT
        #         return JsonResponse(data)
        #获取当前版本号
        version=request.version
        if version=='v1':
            data['results']=ORDER_DICT
        elif version=='v2':
            url=request.versioning_scheme.reverse(viewname='order',request=request)
            data['results']={
                'goods':[
                    {'name':'苹果'},{'name':'香蕉'}
                ],
                'current_url':url
            }
        data['results']=ORDER_DICT
        return JsonResponse(data)
ORDER_DETAIL={
    'name':'苹果',
    'price':'12.2',
    'desc':'好吃'
}



class OrderDetailView(APIView):
    # authentication_classes = [Authentication]

    # permission_classes = [VIPPermission]
    throttle_classes = [UserThrottle]
    """
    用户认证:商品详情页接口，需要用户认证之后才能访问。
    用户权限认证:QQ空间的访问记录(VIP以及VIP以上的等级可以访问)
    """

    def get(self,request):
        data={}
        data['result']=ORDER_DETAIL
        return JsonResponse(data)


from .models import *
#model_to_dict 是将model转化为json
from django.forms.models import model_to_dict
from utils.serializer import *


class RoleView(APIView):
    def get(self,request,*args,**kwargs):
        roles=UserRole.objects.all()
        #使用serializer序列化组件，对roles这个queryset进行转化json的操作。
        #参数：1.需要序列化的对象；2.是一个对象还是多个对象，如果是多个对象必须设置many=True，遍历；一个对象则many=False不遍历。
        serializer=RolesSerializer(instance=roles,many=True)
        #序列化完成，获取最终的json数据
        return Response(serializer.data)

class UserView(APIView):
    """
    用户信息接口类，查询用户信息
    """
    def get(self,request,*args,**kwargs):
        #all().first()是一个，所以many=False
        users=UserInfo.objects.all()
        #对users进行序列化
        serializer=UsersSerializer(instance=users,many=True)
        return Response(serializer.data)

class GroupView(APIView):
    authentication_classes = []
    permission_classes = []
    throttle_classes = []
    def get(self,request,*args,**kwargs):
        groups=UserGroup.objects.all()
        #对groups进行序列化
        serializer=GroupsSerializer(instance=groups,many=True)
        return Response(serializer.data)

class ValicationView(APIView):
    def post(self,request,*args,**kwargs):
        #将前端提交的POST数据，交给序列化类，对数据进行验证，验证成功就返回正确数据，验证失败，抛出异常信息。
        serializer=ValicationSerializer(data=request.data)
        if serializer.is_valid():
            return Response({
                'stauts':'ok',
                'data':serializer.validated_data['password']
            })
        else:
            return Response(serializer.errors)

from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination

#如果使用分页的时候，想要修改查询字符串的参数，可以使用自定义的方式。
class CustomPagincation(PageNumberPagination):
    #定义每页显示的数据个数
    page_size = 2
    #定义查询参数   ?page=1&size=2
    page_size_query_param = 'size'
    #关于页码  ?page=1
    page_query_param = 'page'
    #定义最大返回数据的个数
    max_page_size = 5

class PaginationView(APIView):

    def get(self,request,*args,**kwargs):
        #数据
        users=UserInfo.objects.all()
        #创建分页器对象
        # page=PageNumberPagination()
        # page=LimitOffsetPagination()
        #自定义的CustomPagincation()
        page=CustomPagincation()
        #获取当前页的所有对象
        current_page_users=page.paginate_queryset(users,request)
        #对当前页的对象进行序列化
        serializer=UsersSerializer(instance=current_page_users,many=True)
        # return Response(serializer.data)

        #返回中有上一页、下一页的地址
        return page.get_paginated_response(serializer.data)

from rest_framework.generics import GenericAPIView
class GenericView(GenericAPIView):
    #查询所有数据
    queryset = UserInfo.objects.all()
    #配置序列化的类
    serializer_class = UsersSerializer
    pagination_class = CustomPagincation
    def get(self,request,*args,**kwargs):
        #获取所有的Model对象
        query=self.get_queryset()
        #对所有的Model对象进行分页，获取当前页的数据
        current_page_user=self.paginate_queryset(query)
        #对当前页的数据进行序列化
        serializer=self.get_serializer(instance=self.queryset,many=True)
        return Response(serializer.data)

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin
from rest_framework.routers import DefaultRouter
class GenericViewSetView(RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    """
    GenericViewSet:这个类重写了as_view()函数，这个类之前的请求调用的都是APIView这个类的as_view函数，此时在发送GET请求，调用的是GenericViewSet中的as_view()函数。
    1.这个GenericViewSet类内部已经默认将请求方法(get、post、put、patch)和请求对应的函数做了映射,所以在接口类中不能实现get，post函数类，应该实现请求对应的函数。
    """
    # 查询所有数据
    queryset = UserInfo.objects.all()
    # 配置序列化的类
    serializer_class = UsersSerializer
    pagination_class = CustomPagincation
    # def list(self,request,*args,**kwargs):
    #     users=UserInfo.objects.all()
    #     #对users进行序列化
    #     serializer=UsersSerializer(instance=users,many=True)
    #     serializer= UserModelSerializer(instance=users, many=True)
    #     return Response(serializer.data)
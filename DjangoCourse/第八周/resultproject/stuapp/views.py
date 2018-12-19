from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage,InvalidPage
from django.utils.decorators import method_decorator
import json
from .models import StuModel
from utils.orm_to_json import object_to_json
from utils.allow_origin import allow_origin


from django.middleware.csrf import get_token
def get_csrftoken(request):
    """
    前端访问这个视图，这个视图返回的Response响应头里面会包含Set-Cookie:csrftoken=xxxxxx
    """
    csrf=get_token(request)
    res=JsonResponse({'csrf':csrf})
    return res

#CBV和FBV
#CBV：基于类的视图 class StudentView(View):
#FBV:基于函数的视图 def student(request):
class StudentView(View):
    @method_decorator(allow_origin)
    def get(self,request):
        """
        学生数据查询接口
        功能：分页返回学生数据，前端传递page=1就返回第一页的数据；
        ?page:页码
        ?size:每页的数据个数
        :param request:
        :return:
        """
        error=''
        #1.查询所有的学生数据
        stus=StuModel.objects.all()
        #2.根据前端ajax传递的page&size参数开始做分页数据
        size=int(request.GET.get('size','2'))
        #当前页码
        page_number=int(request.GET.get('page','1'))
        # 2.利用stus数据，创建一个分页器对象
        # 参数1:要分页得数据，参数2:设置每页要展示的数据个数；参数3：如果最后一页不到5个数据，是否将最后一页数据合并到上一页进行展示；默认是False，不合并；
        paginator=Paginator(stus,size)
        # 3.创建页面对象page，每一个page对应的是每一个页面，这个page中包含:
        # a> page.number:表示当前查询的页码
        # b> page.object_list:表示当前页要展示的数据；
        # c>page.paginator:它就是上面创建的Paginator(stus,size)这个对象，无论是哪一页，这个paginator对象始终跟着Page对象；
        try:
            page=paginator.page(page_number)
        except (EmptyPage,PageNotAnInteger,InvalidPage):
            error='已经是最后一页了'
            #默认请求最后一页
            page=paginator.page(paginator.num_pages)
            page_number=paginator.num_pages
        #3.开始做分页
        #假设分页器上只显示5个页码，分页器出现滚动之后，当前页始终在中间，当前页前后各两个页码；
        #总页数小于等于5
        if paginator.num_pages <= 5:
            #全部展示,将当前所有页码的值返回给前端
            page_nums=[x for x in range(1,paginator.num_pages+1)]
        elif page_number < 4:
            #如果总页数超过5页，但是当前页的页码小于4的时候，分页器是同样不会滚动的。
            page_nums=[x for x in range(1,6)]
        elif page_number - 4>=0 and page_number <= paginator.num_pages-2:
            #如果总页数超过5页了，分页器需要滚动
            page_nums=[x for x in range(page_number-2,page_number+3)]
        else:
            #超过5页，但是已经到最后一页了
            page_nums=[x for x in range(paginator.num_pages-4,paginator.num_pages+1)]
        #4.向前端返回json数据
        previous=page.has_previous()
        next=page.has_next()
        data={
            #code状态码，有时候根据这个状态码判断请求是否成功
            'code':100,
            'status':'ok',
            'error':error,
            #总的数据个数
            'total_pages':len(stus),
            #是否有上一页
            'has_previous':previous,
            'previous_url':page_number-1 if previous else None,
            #是否有下一页
            'has_next':next,
            'next_url':page_number+1 if next else None,
            'page_nums':page_nums,
            #当前页的数据列表
            'results':object_to_json(page.object_list),
            #当前页码
            'current_page':page_number
        }
        # response=JsonResponse(data)
        #允许所有源，向这个接口发送请求并得到响应。（改变浏览器默认的禁止跨域，此时就是允许跨域）
        # response['Access-Control-Allow-Origin']='*'
        # return response
        return data

"""
前后端分离的CSRF的问题:
1.在前端分离中，本身就是一种跨站请求，因为这个接口既要被安卓的站点访问，又要被苹果端的站点访问，所以在这种模式下，CSRF认证就失去作用了。解决方案:取消CsrfMilldeware中间件对于CSRF的认证
2.如果在前后端分离中，必须要进行csrf认证，也可以实现；

CSRF工作原理:

FORM表单提交POST请求时
1.每次渲染页面，在Html模板中，{{ csrf_token }}都会加载一个随机字符串，每次的值都是不一样的；这个值会放在请求体FORM Data中，提交至后台；

AJAX提交POST请求时:
不一定非得通过{{ csrf_token }}来认证，也可以通过在请求头中添加X-CSRFToken:csrftoken字段，同样也能通过csrf认证
由于前后端分离：前端页面无法识别{{ csrf_token }},那么前后端分离如何通过csrf认证呢?通过在请求头中，添加X-CSRFToken：csrftoken字段


安装第三方跨域包:pip install django-cors-headers
解决:
1.基本的跨域请求能够实现；
2.能够获取跨域请求返回的响应头中的所有字段(默认只返回Content-Type)；
3.能够在发起跨域请求的时候携带Cookie(默认不允许携带Cookie)
"""
from django.views.decorators.csrf import csrf_exempt,csrf_protect
#csrf_exempt:对某一个FBV(基于函数的视图)的视图取消csrf认证；不能用于CBV
#csrf_protect：对某一个FBV的视图添加csrf认证；不能用于CBV
#如果想让整个项目都取消csrf认证，去settings.py中关闭中间件。
# @csrf_exempt
@csrf_exempt
def add(request):
    pass
class StudentInspectView(View):
    """
    检查学员学号是否唯一的CBV视图类接口。
    """
    @method_decorator(allow_origin)
    def post(self,request):
        stu_id=request.POST.get('sid')
        data={}
        if StuModel.objects.filter(id=stu_id):
            #学号已经存在
            data['is_exist']=1
            data['message']='该学号已经存在'
        else:
            data['is_exist'] = 0
            data['message'] = '该学号可以使用'
        return JsonResponse(data)
class StudentAddView(View):
    def post(self,request):
        sid=request.POST.get('sid')
        name=request.POST.get('name')
        age=request.POST.get('age')
        data={}
        try:
            stu=StuModel()
            stu.id=sid
            stu.name=name
            stu.age=age
            stu.save()
            data['status']='ok'
            data['message']='添加成功'
        except:
            data['status'] = 'error'
            data['message'] = '添加失败'
        return JsonResponse(data)
from django.shortcuts import render,redirect
from django.views.generic import View
from .models import *
# Create your views here.
class NewsTypeView(View):
    """
    新闻类型的View，对应的是/type/路由
    """
    def get(self,request):
        params=''
        try:
            #get()如果获取不到内容会抛出异常，当表单没有提交数据时，get('type')是无法获取值的。或者当输入的关键字在数据库不存在的时候，get也会抛出异常。
            params=request.GET.get('type')
            #1.根据input的参数，获取主表new_type的一条数据。
            if not params:
                return render(request,'list.html',{'result':'请输入查询关键字！'})
            new_type=NewsType.objects.get(type_name=params)
            #2.根据主表的一条数据，查询从表的所有数据。

           #当前的任务就是:根据输入的新闻类型，查询所有属于该类型的新闻信息。
            news=new_type.news_set.all()
            if news:
                #注意:news是一个列表，里面保存的都是News类的对象。
                return render(request,'list.html',{'news':news,'value':params})
            else:
                return render(request,'list.html',{'result':'暂无查询结果'})
        except:
            return render(request,'list.html',{'result':'暂不支持({})类型！'.format(params)})

class NewsDetailView(View):
    """
    问题:同一个通用视图，如何既能处理GET请求，又能处理POST请求，并且GET和POST请求的阐述还不一致。
    """
    def get(self,request,new_id):
        """
        用于处理进入详情页的a标签的GET请求。
        :param request:
        :param new_id:
        :return:
        """
        #根据new_id查询对应新闻对象
        new=News.objects.get(id=new_id)
        #渲染详情页，将new对象，传递到模板中加载数据

        return render(request,'detail.html',{'new':new})
    def post(self,request):
        params = ''
        try:
            params = request.POST.get('title')
            if not params:
                return render(request, 'detail.html', {'result': '请输入查询关键字！'})
            new = News.objects.get(new_name=params)
            if new:
                # return render(request, 'detail.html', {'new': new, 'value': params})
                # 因为render之后，直接渲染详情页detail.html，此时详情页的地址是：/detail/
                # 但是点击a标签也能进行详情页detail.html，此时详情页的地址是：/detail/1/
                # 为了保证地址统一：不使用render()渲染模版函数了，使用redirect()重定向函数
                # redirect是用来切换url地址的，不能用于渲染模版。相当于发起了GET请求。
                return redirect('/detail/{}/'.format(new.id))
            else:
                return render(request, 'list.html', {'result': '暂无查询结果！', 'value': params})
        except:
            return render(request, 'list.html', {'result': '暂不支持({})类型查询！'.format(params)})

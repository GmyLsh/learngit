from django.shortcuts import render
import json,datetime,os
from django.http import JsonResponse,HttpResponse
from django.conf import settings
from .models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage,InvalidPage
from django.db.models import Count
#csrf_exempt：该装饰器是用于视图函数，不适合通用视图。主要就是取消某一个视图函数的csrf认证
#csrf_protect:某一个视图函数需要csrf认证；
"""
当项目90%都不需要csrf认证
将'django.middleware.csrf.CsrfViewMiddleware,这个中间件注释，需要认证的视图函数单独添加装饰器csrf_protect；
当项目90%都需要csrf认证
将'django.middleware.csrf.CsrfViewMiddleware,这个中间件解注释，不需要认证的视图函数的单独添加装饰器csrf_exempt；
'
"""

from django.views.decorators.csrf import csrf_exempt,csrf_protect
@csrf_exempt
def upload_img(request):
    #接受admin后台上传的副文本编辑器上传的图片，将这个图片保存在项目下的uploads目录下；
    result={'error':1,'message':'上传图片失败'}
    #获取副文本编辑器上传的图片
    file=request.FILES.get('imgFile',None)
    if file:
        # 将图片文件写入到本地
        result=image_save(file)
    else:
        #返回错误信息
        result={'error':1,'message':'请选择图片'}
        #content_type='application/json'用于反回json格式的数据
    return HttpResponse(json.dumps(result),content_type='application/json')
def image_save(file):
    #存储图片的函数
    #定义允许上传的图片的类型
    allow_img=['jpg','jpeg','png','gif']
    file_img=file.name.split('.')[-1]
    if file_img not  in allow_img:
        return {'error':0,'message':'图片格式不支持'}
    #在/uploads/下创建一个文件夹，保存副文本上传的图片
    now_date=datetime.datetime.now()
    #利用settings.MEDIA_ROOT和dir拼接图片的上传路径
    dir='kindeditor'+'/%d/%d/'%(now_date.year,now_date.month)
    img_url=settings.MEDIA_ROOT+'/'+dir
    if not os.path.exists(img_url):
        os.makedirs(img_url)
    with open(img_url+file.name,'wb') as f:
        f.write(file.file.read())
    #在拼接上传图片的url地址时，不能返回img_url这个上传路径，需要返回MEDIA_URL这个地址；通过MEDIA_URL映射到MEDIA_ROOT。
    file_url=settings.MEDIA_URL+dir+file.name
    return {'error':0,'url':file_url}

def global_params(request):
    #该函数中用于保存一些全局变量，每个/多个视图函数都要使用并且代码都没有发生变化的变量。所以可以对这些重复性的代码进行优化，直接设置为全局变量，不用在渲染模板的时候每次都传递这些变量。
    # 查询所有分类的信息
    category_list = Category.objects.all()
    # 查询所有广告信息
    ad_list = Ad.objects.all()
    archive_list = Article.objects.archive_date(article_list=Article.objects.all())
    #评论排行
    article_dict_list=Comment.objects.values('article').annotate(count=Count('article')).order_by('-count')
    #根据查询结果集合QuerSet中，根据article的id，取出这个文章的Model对象。
    result_list=[Article.objects.get(id=archive_dict['article'])for archive_dict in article_dict_list]
    if len(result_list)>6:
        result_list=result_list[:6]
    #浏览排行
    #三目运算符:a=if b>c? 10:20
    #if条件成立，则取Article.objects.all().order_by('-click_num')[:6]的值，if条件不成立则取Article.objects.all()的值；
    click_list=Article.objects.all().order_by('-click_num')[:6] if len(Article.objects.all()) else Article.objects.all()
    #标签云
    tag_list=Tag.objects.all()
    return {
        'category_list':category_list,
        'ad_list': ad_list,
        'archive_list': archive_list,
        'comment_list':result_list,
        'click_list':click_list,
        'tag_list':tag_list,
    }
def process_paginator(request,article_list):
    paginator = Paginator(article_list, 1)
    try:
        page_number = int(request.GET.get('page', '1'))
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page = paginator.page(1)
    return page
def index(request):
    #所有文章信息
    article_list=Article.objects.all()
    page = process_paginator(request, article_list)
    title = '最新文章'
    #文章归档：第一种方法就是定义一个普通的函数archive_article
    # archive_list=archive_article(article_list)

    #第二种方法:通过自定义管理器Manager方法实现，通过这种方法，可以实现Article.objects.xxxx()的调用方式;
    #1.在models.py中自定义一个管理器(一定要继承于内置的Manager类。);
    #2.在需要使用的Model类中，注册这个管理器，那么这个Model就可以使用这个管理器方法了;
    # archive_list=Article.objects.archive_date(article_list=article_list)
    return render(request,'index.html',locals())

def archive(request,year,month):
    #查询发布日期中含有:2018-10的数据
    article_list=Article.objects.filter(date_publish__icontains=year+'-'+month)
    page=process_paginator(request,article_list)
    return render(request,'index.html',locals())
# def archive_article(article_list):
#     archive_list=[]
#     for archive in article_list:
#         #将每一个文章的发布日期都获取出来，按照'%Y/%m'进行格式化
#         pub_date=archive.date_publish.strftime('%Y/%m')
#         if pub_date not in archive_list:
#             #如果这个时间字符串不在article_list这个列表里面就把这个年月添加进去
#             archive_list.append(pub_date)
#     return archive_list

from django.shortcuts import render
from django.views.generic import View
from .models import Advertising,Label,Article,Sort
from django.db.models import Count
from django.core.paginator import PageNotAnInteger,Paginator,InvalidPage,EmptyPage
# Create your views here.
class AdvertisingView(View):
    def get(self,request):
        sort=Sort.objects.all()
        ad_list=Advertising.objects.all()
        label=Label.objects.all()
        article=Article.objects.all()

        #浏览排行
        a_look=Article.objects.values('a_title').annotate(count=Count('a_title')).order_by('-a_look')
        list1=[]
        for look in a_look:
            list1.append(look['a_title'])
        #评论排行
        a_comment=Article.objects.values('a_title').annotate(count=Count('a_title')).order_by('-a_comment')
        list2=[]
        for comment in a_comment:
            list2.append(comment['a_title'])
        #站长推荐
        ID=Article.objects.values('a_title').annotate(count=Count('a_title')).order_by('-id')
        list3=[]
        for d in ID:
            list3.append(d['a_title'])

        Id=Article.objects.values('id').annotate(count=Count('id'))
        list4=[]
        for x in Id:
            list4.append(x['id'])
        res=list4[-1]
        paginator=Paginator(article,1)
        try:
            page_number=request.GET.get('page','1')
            page = paginator.page(page_number)
        except (PageNotAnInteger,EmptyPage,InvalidPage):
            page=paginator.page(1)
        return render(request,'index.html',locals())

class ArticView(View):
    def get(self,request):
        article = Article.objects.all()
        return render(request,'artic.html',locals())
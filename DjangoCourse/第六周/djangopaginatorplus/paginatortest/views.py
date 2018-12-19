from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

from .models import UserModel


def add(request):
    for x in range(1, 201):
        name = '张三{}'.format(x)
        age = 100 + x
        user = UserModel(name=name, age=age)
        user.save()

    return HttpResponse('ok')


def select(request):
    users = UserModel.objects.all()
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page', '1')
    try:
        page = paginator.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        page = paginator.page('1')
    return render(request, 'index.html', {'page': page})
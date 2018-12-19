from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'nav.html',{'index':index})
def add(request):
    return render(request,'add.html',{'add':add})
def update(request):
    return render(request,'update.html',{'update':update})
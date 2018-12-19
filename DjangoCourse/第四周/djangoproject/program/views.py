from django.shortcuts import render

# Create your views here.
def program_add(request):
    return render(request,'program/add.html')
def program_detail(request):
    return render(request,'program/detail.html')
def program_edit(request):
    return render(request,'program/edit.html')
def program_list(request):
    return render(request,'program/list.html')
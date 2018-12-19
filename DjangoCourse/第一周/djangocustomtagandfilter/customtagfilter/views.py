from django.shortcuts import render

# Create your views here.
#如何自定义Django模板语言中的标签和过滤器
# 1.在app下或者在项目根目录下新建包文件夹:templatetags(名字固定)；
# 2.在这个包里面新建一个.py文件，名称自定义；
def customtagfilter(request):
    return render(request,'index.html',{'name':'张三'})

from django.shortcuts import render

# Create your views here.
"""
模板继承:对于一个网站来说，会存在很多的.html文件，但是由于一些页面中会有相同的页面结构出现，也就导致了多个html文件中代码是重复的，所以为了在html中减少重复的代码出现，简化html结构，可以将多个页面中相同的html代码，单独的抽离出来放在一个html文件中，其他的html文件如果想要使用这部分内容，直接继承过去可以了。有点类似于类的继承关系。
继承关系中：父模板和子模板。

Django如何在html中引用静态文件?
1.在项目根目录下或者APP下，新建一个static文件夹(名字是固定的)；将所有的静态资源文件放进去；
2.如果static放在根目录下创建的，需要在settings.py中，配置搜索路径；如果是在APP下创建的，不用配置；
3.在html文件中，引入静态资源；
"""
def func_index(request):
    return render(request,'index.html')
def func_list(request):
    return render(request,'list.html')
def func_detail(request):
    return render(request,'detail.html')
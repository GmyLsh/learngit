from django.shortcuts import render
import datetime
# Create your views here.
#模板的渲染：视图函数再返回Response的时候，返回的是一个html文件，并且会传递一些数据给html，最终将这些数据展示在页面中，
#Django中提供了一个templates文件夹，用于存放所有的html文件。
#templates文件夹的创建位置:
#1.在项目根目录下创建：这种情况整个项目中只有一个templates文件夹，供所有的APP使用
#2.分模块，在各自的APP下创建templates文件将夹
def index(request):
    #render:渲染
    #模板:html文件
    #template_name：指定要渲染的模板的名称。
    return render(request, template_name='templates/index.html')

#如果是将templates文件夹放在了每一个APP下，要注意模块可能会引用出错，引用到其他APP下的模板文件。
#模板的查找顺序:
#1.模板的查找顺序是先从根目录下的templates文件中查找，如果根目录下没有templates文件夹/或者说根目录下没有找到需要的模板
# 2.此时Django会去自己APP下templates中找模板，如果自己APP下的templates中没有这个模板，再去其他app下的templates中查找，
# 3.如果最终所有的templates中都没有找到所需要的模板，就会抛出异常，说模板不存在 TemplateDontExisted

#解决办法:在各自app下的templates文件夹中，再新建一个文件夹，用于区分文件名相同的html模板文件。
class People(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_name(self):
        return '我的名字是:{}'.format(self.name)
def html_data(request):
    """
    如何在渲染模板的时候，向模板传递数据。
    能够传递的数据:
    字符串
    列表
    字典
    对象
    数字类型
    :param request:
    :return:
    """
    p=People('李四',25)
    # context：上下文，负责向模板传递数据。
    #render/index.html:render不是代表APP的名称，是templates文件夹下的一个文件夹的名称，这个名称可以随便定义。只是当前是和APP的名称重复了。
    return render(request, template_name='render/index.html',context={
        'name':'陈罗文',
        'books':['HTML','JS','CSS','PYTHON',100,200,True],
        'date':datetime.datetime.now(),
        'object':p,
        'dict':{'username':'haha','password':'123'},
        'input':'<h1>这是一个h1标签字符串</h1>',
    })
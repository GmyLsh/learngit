from django.shortcuts import render
from django.http import HttpResponse
from .forms import CustomForm
# Create your views here.
def index(request):
    #当加载首页index.html的时候，不再使用默认的form表单了，需要将CustForm这个定制的表单，渲染到index.html中。
    form=CustomForm()
    return render(request,'index.html',{'form':form})
def form(request):
    """
    计算<form>表单中a和b相加之后的值。
    :param request:
    :return:
    """
    if request.method=="GET":
        #此时的url地址:/form/?a=1&b=2
        #获取form表单的GET请求的参数
        a = request.GET.get('a',0)
        b = request.GET.get('b',0)
        return HttpResponse('结果：{}'.format(int(a)+int(b)))
    elif request.method=="POST":
        #如果是表单(CustomForm)提交的是POST请求，如何获取POST请求的参数?
        #两种方式：1.request.POST.get();2.使用is_valid()
        # print(request.POST)
        #根据POST请求的数据，初始化CustomForm类的对象。
        form = CustomForm(data=request.POST)
        #cleaned_data:如果CustomForm表单数据是合法的，那么input标签中的值，都会被放入cleaned_data这个字典中，如果CustomForm表单数据是不合法的，那么cleaned_data字典就不存在。
        #注意：在使用cleaned_data之前，一定要通过is_valid()判断数据的合法性。否侧cleaned_data这个字典就是不存在的。只有通过is_valid()验证之后，才会生成这个cleaned_data字典。
        if form.is_valid():
            a=form.cleaned_data['a']
            b=form.cleaned_data['b']
            return HttpResponse(a+b)
        else:
            #如果不合法，将错误信息展示到页面上。
            #此时的form对象中，携带异常信息的form
            return render(request,'index.html',{'form':form})

#Django框架的form表单，除了提供基本的请求，还提供了一套用于验证input中填写的数据是否合法的规则。比如:要求填写数字，但是填写的是字母，就会被Django中的form的验证机制识别为数据不合法。数据是否合法指的是form预先设定的类型或者数据长度是否和输入的数据类型和长度保持一致。

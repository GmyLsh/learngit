from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    """
    index视图函数对应了两个请求:
    1.访问天气首页，发起的GET请求；
    2.提交form表单，发起的GET请求；
    a> 上述情况可以使用：请求是否携带参数区分这两个GET请求；
    b> 使用不同的请求，来区分是刷新首页还是form请求。
    :param request:
    :return:
    """
    # try:
    #     current_city=request.GET['city']
    # except:
    #     #访问首页路由，除了渲染html页面之外，还需要提供一个默认城市的天气
    #     current_city='郑州市'
    #访问首页路由，除了渲染html页面之外，换需要提供一个默认城市的天气

    if request.method=='GET':
        #如果是GET请求，说明是刷新首页
        current_city='郑州市'
    else:
        #如果是POST请求，说明是form表单请求
        #'city'获取的是weather.html里面input里面的name即网页上的输入框
        current_city=request.POST.get('city')
    url='http://api.map.baidu.com/telematics/v3/weather?location={}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'.format(current_city)
    data=requests.get(url).json()
    weather_data=data['results'][0]['weather_data']
    return render(request,'weather.html',{'weather_data':weather_data,'current_city':current_city})

#问题:
# 1.同一个视图函数如何处理同一个请求?
# 2.同一个视图函数如何处理不同的请求?


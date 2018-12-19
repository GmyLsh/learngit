from django.shortcuts import render

# Create your views here.
# coding:utf-8
from django.shortcuts import render
# 引入响应类
from django.http import HttpResponse
# 引入requests
import requests
# 引入json包
import json


# Create your views here.
# 视图函数  必须携带一个request参数
def index(request):
    # 判断请求的方式是get还是post，如果是get请求，返回郑州市的天气信息，如果是post请求，取出城市名称，拿回对应的天气信息
    if request.method == 'GET':
        city = '郑州市'
    elif request.method == 'POST':
        city = request.POST.get('city')
        if city == '':
            city = '郑州市'

    # 返回响应对象
    # return HttpResponse('<h1 style="color:red;">hello world</h1>')
    url = 'http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'%city
    response = requests.get(url)
    # 把json数据转换为python中的字典
    weather = json.loads(response.text)
    # 判断返回的数据中error是否为0，为0表示查询结果是正常的
    if weather['error'] == 0:
        # 取出天气情况列表
        info = weather['results'][0]
        # 取出当前城市
        currentCity = info['currentCity']
        weather_data = info['weather_data']
        # 组装填充网页信息的字典
        result = {
            'currentCity': currentCity,
            'weather_data': weather_data
        }
        # 1.请求  2.模板文件名称 3.返回填充网页的数据
        return render(request, 'weather.html', result)
    else:
        return HttpResponse('<h1 style="color:red;text-align:center;"><a href="/">您查询的城市没有天气信息！</a></h1>')

from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    #使用IP定位接口，当第一次访问页面的时候，根据IP定位的城市，解析这个城市的最新电影信息。
    try:
        #如果GET请求是:http://localhost:8000/index/?city=180,第一次是可以获取city的值。
        #这个GET请求获取的是页面中<input>标签的输入的值，但是在第一次请求的时候，页面并没有被渲染出来，是无法获取这个值的。
        city=request.GET['city']
    except:
        ip_url='https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z'
        result=requests.get(ip_url).json()
        city=result['content']['address_detail']['city']

    movie_url='http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location=郑州市&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
    movie_data=requests.get(movie_url).json()
    if movie_data['status']!='Success':
        context={
            'error':'请求出现错误'
        }
    else:
        movies=movie_data['result']['movie']
        if movies:
            context={
                'city':city,
                'movies':movies
            }
        else:
            context={
                'city':city,
                'error':'当前城市没有查询到最新电影信息！'
            }
    return render(request,'movie.html',context=context)
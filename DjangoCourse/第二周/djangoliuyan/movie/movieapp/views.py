from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    city_url='https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z'
    city=requests.get(city_url).json()
    if request.method=="GET":
        #第一次发起请求或者刷新首页都是GET请求。
        current_city = city['content']['address_detail']['city']
    else:
        current_city=request.POST.get('city')
    url='http://api.map.baidu.com/telematics/v3/movie?qt=hot_movie&location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(current_city)
    data = requests.get(url).json()
    movie_data=data['result']['movie']
    return render(request,'movie.html',{'movie_data':movie_data,'current_city':current_city})
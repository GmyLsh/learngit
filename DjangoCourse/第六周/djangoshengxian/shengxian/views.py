from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.core.paginator import PageNotAnInteger,Paginator,InvalidPage,EmptyPage
from django.db.models import Count
# Create your views here.
#网站首页
def index(request):
    username = request.session['username']
    food_type=FoodType.objects.all()
    if ShopCart.objects.filter(is_active=0):
        shop = ShopCart.objects.filter(is_active=0)
        str_a = '0'
        for sh in shop:
            a = sh.shop_code
            str_a = int(str_a) + int(a)
        return render(request, 'index.html', locals())
    else:
        return render(request,'index.html',locals())
#商品列表页
def list_page(request):
    username = request.session['username']
    if username:
        type_id=request.GET.get('type')
        food_type=FoodProduct.objects.filter(sort_id=type_id)
        paginator=Paginator(food_type,2)
        page_number = request.GET.get('page', '1')
        try:
            page=paginator.page(page_number)
        except (PageNotAnInteger,EmptyPage,InvalidPage):
            page=paginator.page(1)
        return render(request,'list.html',locals())
    else:
        return render(request,'login.html')
#商品详情页
def detail(request):
    username = request.session['username']
    type_id=request.GET.get('type')
    food_id = request.GET.get("detail")
    sort_shop=FoodProduct.objects.filter(sort_id=type_id)
    food_type=FoodType.objects.all()
    shop_detail=ShopDetail.objects.get(food_name_id=food_id)
    food=FoodProduct.objects.get(id=food_id)
    if ShopCart.objects.filter(is_active=0):
        shop = ShopCart.objects.filter(is_active=0)
        str_a = '0'
        for sh in shop:
            a = sh.shop_code
            str_a = int(str_a) + int(a)
        return render(request, 'detail.html', locals())
    else:
        return render(request,'detail.html',locals())
#注册页面
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method=='POST':
        nickname=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('pwd')
        if UserModels.objects.filter(nickname=nickname):
            return render(request,'register.html',{'error':'用户名已被注册'})
        user=UserModels()
        user.email=email
        user.nickname=nickname
        user.name_password=password
        user.save()
        return render(request,'login.html')
#登录页面
def login_fun(request):
    if request.method =='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        name=request.POST.get('username')
        pwd=request.POST.get('pwd')
        try:
            #QuerSet是一个对象
            user=UserModels.objects.get(nickname=name)
        except Exception as e:
            return render(request,'login.html',e)
        if pwd==user.name_password:
            request.session['username'] = user.nickname
            request.session['id']=user.id
            return redirect('/user_center_info/')
        return render(request,'login.html',{'error':'用户名或者密码错误！'})
#用户中心-用户信息页
def user_center_info(request):
    try:
        user_name = request.session['username']
    except:
        return render(request,'login.html')
    if user_name:
        phone_T=UserModels.objects.get(nickname=user_name)
        try:
            address=UserInfo.objects.filter(user_name_id=phone_T.id)
        except:
            pass
        return render(request, 'user_center_info.html', locals())
    else:
        return render(request,'login.html')
#用户中心-用户订单页
def user_center_order(request):

    return render(request,'user_center_order.html')
#用户中心-用户收货地址页
def user_center_site(request):
    username = request.session['username']
    user_1 = UserModels.objects.get(nickname=username)
    if request.method=='GET':
        try:
            address = UserInfo.objects.filter(user_name_id=user_1.id)
        except :
            return render(request, 'user_center_site.html',{'error':'请填写地址'})
        return render(request,'user_center_site.html',locals())
    elif request.method=='POST':
        #收件人
        receiver=request.POST.get('receiver')
        #详细地址
        deta_address=request.POST.get('deta_address')
        #邮编
        postcode=request.POST.get('postcode')
        #电话
        login_user = UserModels.objects.get(nickname=request.session.get("username"))
        phone=request.POST.get('phone')
        user=UserInfo()
        user_id=user.id
        user.receiver=receiver
        user.address=deta_address
        user.post_code=postcode
        user.phone=phone
        user.user_name_id=login_user.id
        user.save()
        return render(request,'user_center_site.html',locals())
#接受ajax传过来的数据
def shop_cart(request):
    username=request.session['username']
    if username:
        if request.is_ajax():
            food_name_id = request.GET['food_name_id']
            food_produce = FoodProduct.objects.get(id=food_name_id)
            if ShopCart.objects.filter(food_name_id=food_name_id,is_active=0):
                # None get
                # QuerySet[2] filter
                add_or_minus = request.GET['add_or_minus']
                if add_or_minus=='1':
                    food_id = request.GET['food_name_id']
                    food = FoodProduct.objects.get(id=food_id)
                    user_1=ShopCart.objects.get(food_name_id=food_id)
                    user_1.shop_code+=1
                    user_1.shop_price=food.food_price
                    user_1.shop_price_total+=food.food_price
                    user_1.save()
                    return HttpResponse('ok')
                elif add_or_minus=='0':
                    food_id = request.GET['food_name_id']
                    food = FoodProduct.objects.get(id=food_id)
                    user_1 = ShopCart.objects.get(food_name_id=food_id)
                    user_1.shop_code -= 1
                    user_1.shop_price = food.food_price
                    user_1.shop_price_total -= food.food_price
                    user_1.save()
                    return HttpResponse('ok')
                elif add_or_minus=='2':
                    user_1 = ShopCart.objects.get(food_name_id=food_name_id)
                    user_1.delete()
                    return HttpResponse('ok')
            else:
                nickname_id = request.session['id']
                shop_price = request.GET['price']
                code = request.GET['code']
                user = ShopCart()
                user.shop_name_id = food_name_id
                user.shop_code = int(code)
                user.food_name_id = food_name_id
                user.nickname_id = nickname_id
                user.shop_price = int(shop_price)
                user.shop_price_total = int(shop_price)
                user.save()
                return render(request,'list.html',locals())
        return render(request,'cart.html')
    return render(request, 'login.html')
#我的购物车页面
def cart(request):
    username = request.session['username']
    if username:
        if ShopCart.objects.filter(is_active=0):
                shop=ShopCart.objects.filter(is_active=0)
                str_a = '0'
                str_b='0'
                for sh in shop:
                    a=sh.shop_code
                    b=sh.shop_price_total
                    str_a = int(str_a)+int(a)
                    str_b=int(str_b)+int(b)
                return render(request,'cart.html',locals())
        else:
            return render(request,'cart.html',{'str_a':'0'})
#提交订单页面
def place_order(request):
    username = request.session['username']
    user_1 = UserModels.objects.get(nickname=username)
    try:
        address = UserInfo.objects.filter(user_name_id=user_1.id)
    except:
        return render(request, 'user_center_site.html', {'error': '请填写地址'})
    if username:
        if ShopCart.objects.filter(is_active=0):
                shop=ShopCart.objects.filter(is_active=0)
                str_a = '0'
                str_b='0'
                str_c='0'
                for sh in shop:
                    a=sh.shop_code
                    b=sh.shop_price_total
                    str_a = int(str_a)+int(a)
                    str_b=int(str_b)+int(b)
                str_c=int(str_c)+str_b+10
                return render(request,'place_order.html',locals())
        else:
            return render(request,'place_order.html',{'str_a':'0'})
    return render(request,'place_order.html',locals())
def logout_out(request):
    request.session.flush()
    return redirect('/login/')


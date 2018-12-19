from django.db import models

# Create your models here.


class UserModels(models.Model):
    nickname = models.CharField(max_length=100,verbose_name='用户昵称')
    name_password=models.CharField(max_length=100,verbose_name='用户密码')
    email=models.EmailField(verbose_name='邮箱')


class UserInfo(models.Model):
    phone=models.IntegerField(max_length=20,null=True,verbose_name='联系方式')
    address = models.CharField(max_length=50, null=True,verbose_name='联系地址')
    post_code=models.IntegerField(max_length=20,null=True,verbose_name='邮编')
    receiver=models.CharField(max_length=20,null=True,verbose_name='收件人')

    user_name=models.ForeignKey(UserModels,on_delete=models.DO_NOTHING,verbose_name='用户名',blank=True,null=True)

class FoodType(models.Model):
    sort=models.CharField(max_length=100,verbose_name='商品分类')
    class Meta:
        verbose_name='分类'
        verbose_name_plural=verbose_name
    def __str__(self):
        return self.sort


class FoodProduct(models.Model):
    food_name=models.CharField(max_length=100,verbose_name='商品名称')
    food_price=models.IntegerField(default=0,verbose_name='商品价格')
    food_count=models.IntegerField(default=0,verbose_name='商品库存')
    food_image=models.ImageField(upload_to='uploads/%Y/%m')
    sort=models.ForeignKey(FoodType,verbose_name='所属分类',on_delete=models.DO_NOTHING,blank=True,null=True)
    class Meta:
        verbose_name='商品'
        verbose_name_plural=verbose_name
        ordering=['-food_price']
    def __str__(self):
        return self.food_name
class ShopDetail(models.Model):
    shop_detail=models.CharField(max_length=100,verbose_name='商品详情')
    shop_intro=models.CharField(max_length=100,verbose_name='商品简介')
    food_name=models.ForeignKey(FoodProduct,verbose_name='所属商品',on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self):
        return self.shop_detail
    class Meta:
        verbose_name='商品详情'
        verbose_name_plural=verbose_name


class ShopCart(models.Model):
    is_active=models.IntegerField(default=0,verbose_name='为1购物车清空')
    shop_code=models.IntegerField(null=True, verbose_name='购买商品数量')
    shop_price=models.IntegerField(null=True,verbose_name='商品单价')
    shop_price_total=models.IntegerField(null=True,verbose_name='小计')
    nickname=models.ForeignKey(UserModels,verbose_name='添加购物车用户',on_delete=models.DO_NOTHING,blank=True,null=True)
    food_name=models.ForeignKey(FoodProduct,verbose_name='购物车添加商品',on_delete=models.DO_NOTHING,blank=True,null=True)
    add_shop_time=models.DateTimeField(auto_now_add=True,editable=True,verbose_name='添加购物车的时间')

    def __str__(self):
        return self.nickname
    class Meta:
        verbose_name='购物车'
        verbose_name_plural=verbose_name
class Order(models.Model):
    add_order_time=models.DateTimeField(auto_now_add=True,editable=True,verbose_name='生成订单时间')
    order_branch=models.IntegerField(null=True,verbose_name='订单号')
    payment_status=models.CharField(max_length=50,verbose_name='支付状态')
    shop_cart=models.ForeignKey(ShopCart,verbose_name='关联的购物车',on_delete=models.DO_NOTHING,blank=True,null=True)
    food_produce=models.ForeignKey(FoodProduct,verbose_name='关联商品',on_delete=models.DO_NOTHING,blank=True,null=True)
    def __str__(self):
        return self.order_branch
    class Meta:
        verbose_name='订单'
        verbose_name_plural=verbose_name
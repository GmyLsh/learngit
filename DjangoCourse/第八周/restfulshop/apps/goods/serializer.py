from rest_framework import serializers

class GoodsSerilizer(serializers.Serializer):
    """
    Serializer:序列化的基类，虽然写起来麻烦，但是定制性高
    """
    name=serializers.CharField()
    aold_num=serializers.IntegerField(default=0)
    goods_front_image=serializers.IntegerField()
    shop_price=serializers.CharField()
    add_time=serializers.DateTimeField()
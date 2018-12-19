from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *
#serializer:序列化数据、对数据进行验证
class GoodsListView(APIView):
    """
    商品列表页接口
    """
    def get(self,request):
        #查询商品列表接口
        goods=Goods.objects.all()[:10]
        serializer= GoodsSerilizer(instance=goods,many=True)
        return Response(serializer.data)
    def post(self,request):
        #添加商品接口
        pass
from rest_framework import serializers
from .models import Goods
from .models import GoodsCategory
class CateGorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class GoodsSerializer(serializers.ModelSerializer):
    # category = CateGorySerializer()
    class Meta:
        model = Goods
        fields = '__all__'
        depth = 1

from django.views.generic.base import View
from goods.models import Goods

class GoodsListView(View):
    def get(self,request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods = Goods.objects.all()
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)
        from django.http import HttpResponse
        from django.core import serializers
        import json
        json_data = serializers.serialize('json',goods)
        json_data = json.loads(json_data)

        return HttpResponse(json_data, content_type="application/json")

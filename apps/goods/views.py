from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from goods.models import Goods
from goods.serializer import GoodsSerializer
from django.http import Http404
from rest_framework import status
from rest_framework import mixins,generics
# Create your views here.
class GoodsListView(generics.ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    # def get(self, request, *args,**kwargs):
    #     return self.list(request,*args,**kwargs)


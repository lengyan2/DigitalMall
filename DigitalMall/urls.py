"""DigitalMall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
import xadmin
from DigitalMall.settings import MEDIA_ROOT
from django.views.static import serve
from apps.goods.views import GoodsListView
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),

    # 商品列表页
    url(r'goods/$',GoodsListView.as_view(),name='good-list'),

    url(r'docs/',include_docs_urls(title='数码商城')),
    path('api-auth/', include('rest_framework.urls')),
]

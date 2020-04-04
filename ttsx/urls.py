from cart.views import add_cart
from django.conf.urls import url
from django.contrib import admin
from goods.views import index, detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 第一个参数是要访问的URL地址匹配的正则表达式 参数2是要访问的视图的函数
    url(r'^index/$', index),#主页
    url(r'^detail/$', detail),#详情页
    url(r'^cart/add_cart/$', add_cart),
]

from django.shortcuts import render, redirect


# Create your views here.
def add_cart(request):
    """添加到购物车 cookie  goods_id :count"""
    #1 获取传过来的商品ID
    goods_id = request.COOKIES.get('id','')
    #2 将商品ID存储到cookie里
        # 实例化redirect对象
    if goods_id:
        prev_url = request.META('HTTP_REFERER')
        respones = redirect(prev_url)
        goods_count = request.COOKIES.get(goods_id)
        # 如果之前购物车里有商品那么就在之前的数量上加1
        if goods_count:
            goods_count = int(goods_count) +1
        # 如果之前没有那么就添加一个
        else:
            goods_count = 1
        # 把商品id保存到cookie
        respones.set_cookie(goods_id, goods_count)

    return respones
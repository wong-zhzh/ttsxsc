from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# 视图就是一个函数
# 必须传一个请求 request 请求对象 里面有用户发送的请求信息 比如一个url地址和其他数据
from goods.models import GoodsCategory, GoodsInfo

'''首页视图函数'''


def index(request):
    # 1 查询商品分类
    categories = GoodsCategory.objects.all()
    # 2 从每个分类中获取4个商品 （获取每一类最后四个最新商品）
    for cag in categories:
        # goodinfo= GoodsInfo.objects.filter(goods_cag=)
        # 一对多关系，查询多的一方，会在一的一方有一个属性，多的一方模型类小写_set
        # cag.goodsinfo_set.all()
        # order_by 是排序，这里是根据ID排序     - 表示反向排序（大->小），切片代表前四个
        cag.goods_list = cag.goodsinfo_set.order_by('-id')[:4]
    # 3 获取购物车里所有的商品cookie key : value  == 商品id ： 数量
    # 购物车商品列表
    cart_goods_list = []
    # 4 购物车商品数量
    cart_goods_count = 0
    for goods_id, goods_num in request.COOKIES.items():
        # 通过判断来验证当前是不是商品数据，如果不是 跳过本次循环
        if not goods_id.isdigit():
            continue
        # 获取当前遍历的商品的对象
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        cart_goods.goos_num = goods_num
        # 把商品存放在列表里
        cart_goods_list.append(cart_goods)
        # 累加所有商品数量 goods_num 是字符串 需要强转为int类型
        cart_goods_count = cart_goods_count + int(goods_num)

    # 参数1 是请求的对象request ，参数二是需要返回的HTML页面 ，参数三是需要传入模板里的数据
    return render(request, 'index.html', {'categories': categories,
                                          'cart_goods_list': cart_goods_list,
                                          'cart_goods_count': cart_goods_count})


'''商品详情页面视图函数'''


def detail(request):
    # 商品分类
    cactegory = GoodsCategory.objects.all()
    # 购物车数据
    # 所有的购物车商品
    cartgoods_list = []
    # 购物车商品的总数量
    cartgoods_count = 0

    # 去cookie取数据 goods_id :count
    for goods_id, goods_num in request.COOKIES.items():
        # 验证是不是商品
        if not goods_id.isdigit():
            continue
        # 根据ID查询商品
        cart_goods = GoodsInfo.objects.get(id=goods_id)
        # 把商品数量存放在商品对象中
        cart_goods.goods_num = goods_num
        # 把商品添加到商品列表中
        cartgoods_list.append(cart_goods)
        # 累加所有的商品数量，得到总数量
        cartgoods_count += int(goods_num)
        # 当前要显示的商品数据
        # 获取传过来的商品的id
    goods_id = request.GET.get('id', 1)
    goods_data = GoodsInfo.objects.get(id=goods_id)

    return render(request, 'detail.html', {'cactegory': cactegory,
                                               'cart_goods_list': cartgoods_list,
                                               'cart_goods_count': cartgoods_count,
                                               'goods_data': goods_data})

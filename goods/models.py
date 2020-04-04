from django.db import models

# Create your models here.
# 商品分类表
# 模型类  对应了一张表
class GoodCategory(models.Model):
    # 分类名称 max_length=30 字符串类型必须定义
    cag_name = models.CharField(max_length=30)
    # 分类样式
    cag_css = models.CharField(max_length=20)
    # 分类图片 图片在服务器中路径
    cag_img = models.ImageField(upload_to='cag')
# 商品表
class GoodsInfo(models.Model):
    # 商品名字
    goods_name = models.CharField(max_length=100)
    # 商品价格
    goods_price = models.IntegerField(default=0)
    # 商品描述
    goods_desc = models.CharField(max_length=2000)
    # 商品图片
    goods_img = models.ImageField(upload_to='goods')
    # 所属分类
    goods_cag = models.ForeignKey('GoodCategory')

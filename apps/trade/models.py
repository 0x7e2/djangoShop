from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


# Create your models here.

class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name=u"商品", on_delete=models.CASCADE)
    nums = models.IntegerField(default=0, verbose_name=u"购买数量")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class OrderInfo(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "交易成功"),
        ("TRADE_CLOSED", "超时关闭"),
        ("WAIT_BUYER_PAY", "交易创建"),
        ("TRADE_FINISHED", "交易结束"),
        ("paying", "待支付")
    )
    PAY_TYPE = (
        ("alipay", "成功"),
        ("wechat", "微信")
    )
    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.CASCADE)
    order_sn = models.CharField()
    trade_on = models.CharField()
    pay_status = models.CharField()
    order_mount = models.FloatField()
    pay_time = models.DateTimeField()

    # 用户信息
    address = models.CharField()
    singer_name = models.CharField()
    singer_mobile = models.CharField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)

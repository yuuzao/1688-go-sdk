# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class TradeOrderModifyOrderPriceParam(BaseApi):
    """修改订单价格，注意：订单价格修改逻辑同1688后台页面，是在订单原价的基础之上计算总价，不是在原先的折扣后的总价基础之上再增加或减少价格，对于订单已经存在在折扣是覆盖的。
entryDiscounts不需要已经关闭的子订单信息。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=trade.order.modifyOrderPrice&v=1&cat=aop.trade

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.orderId = None
        self.carriage = None
        self.entryDiscounts = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/trade.order.modifyOrderPrice'

    def get_required_params(self):
        return ['orderId', 'carriage', 'entryDiscounts']

    def get_multipart_params(self):
        return []

    def need_sign(self):
        return True

    def need_timestamp(self):
        return False

    def need_auth(self):
        return True

    def need_https(self):
        return False

    def is_inner_api(self):
        return False

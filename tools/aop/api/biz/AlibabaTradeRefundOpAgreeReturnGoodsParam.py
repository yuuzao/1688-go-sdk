# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaTradeRefundOpAgreeReturnGoodsParam(BaseApi):
    """卖家同意退货，并填写退货地址信息。注意：只有退货的售中或者售后退款单，才可以调用这个接口。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=alibaba.trade.refund.OpAgreeReturnGoods&v=1&cat=aop.trade

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.refundId = None
        self.address = None
        self.post = None
        self.phone = None
        self.fullName = None
        self.mobilePhone = None
        self.discription = None
        self.disputeType = None

    def get_api_uri(self):
        return '1/com.alibaba.trade/alibaba.trade.refund.OpAgreeReturnGoods'

    def get_required_params(self):
        return ['refundId', 'address', 'post', 'phone', 'fullName', 'mobilePhone', 'discription', 'disputeType']

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

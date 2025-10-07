# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class OrderAepickuporderCheckSendAddressParam(BaseApi):
    """检查订单发货地址是否一致


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.orderIds = None

    def get_api_uri(self):
        return '1/com.alibaba.supplychain/order.aepickuporder.checkSendAddress'

    def get_required_params(self):
        return ['orderIds']

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

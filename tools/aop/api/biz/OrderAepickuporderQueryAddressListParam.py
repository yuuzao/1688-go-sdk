# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class OrderAepickuporderQueryAddressListParam(BaseApi):
    """查询商家发货地址列表


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None

    def get_api_uri(self):
        return '1/com.alibaba.supplychain/order.aepickuporder.queryAddressList'

    def get_required_params(self):
        return []

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

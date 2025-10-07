# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class CarriagecenterReceivingBySellerGetParam(BaseApi):
    """商家索要收货码


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.apiOrderId = None
        self.apiLogisticsId = None

    def get_api_uri(self):
        return '1/com.alibaba.logistics/carriagecenter.receivingBySeller.get'

    def get_required_params(self):
        return ['apiOrderId', 'apiLogisticsId']

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

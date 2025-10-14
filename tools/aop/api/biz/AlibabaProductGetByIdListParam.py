# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductGetByIdListParam(BaseApi):
    """根据商品ID列表获取卖家的商品。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.getByIdList&v=1&cat=aop.product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productIdList = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.getByIdList'

    def get_required_params(self):
        return ['productIdList']

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

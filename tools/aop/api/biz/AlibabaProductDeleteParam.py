# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductDeleteParam(BaseApi):
    """将某个商品删除到回收站中，可在网站手工清除或恢复。此API为国际站与1688通用。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.delete&v=1&cat=aop.product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productID = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.delete'

    def get_required_params(self):
        return ['productID']

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

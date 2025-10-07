# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductGetParam(BaseApi):
    """由商品ID获取商品详细信息，请注意：只能查询自己所有的产品。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.get&v=1&cat=product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productID = None
        self.webSite = None
        self.scene = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.get'

    def get_required_params(self):
        return ['productID', 'webSite', 'scene']

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

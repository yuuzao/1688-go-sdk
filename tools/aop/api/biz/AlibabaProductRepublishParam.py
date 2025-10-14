# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductRepublishParam(BaseApi):
    """未上架商品重新上架。请注意：会员每天最多上架400条，非诚信通或者买家保障会员，食品美容行业如果有限制，则不能上架，橡塑现货条数限制，已上网最多200条。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.republish&v=1&cat=product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productIds = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.republish'

    def get_required_params(self):
        return ['productIds']

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

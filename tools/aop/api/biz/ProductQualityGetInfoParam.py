# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class ProductQualityGetInfoParam(BaseApi):
    """获取商品质量星级相关信息

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=product.quality.getInfo&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.catId = None
        self.dataBody = None
        self.offerId = None
        self.scene = None
        self.bizParam = None

    def get_api_uri(self):
        return '1/com.alibaba.product/product.quality.getInfo'

    def get_required_params(self):
        return ['catId', 'dataBody', 'offerId', 'scene', 'bizParam']

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

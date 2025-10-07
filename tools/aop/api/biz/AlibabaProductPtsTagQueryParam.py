# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductPtsTagQueryParam(BaseApi):
    """查询该商品开通了买家保障中的哪些服务

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.ptsTag.query&v=1&cat=product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.offerId = None
        self.subCategoryId = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.ptsTag.query'

    def get_required_params(self):
        return ['offerId', 'subCategoryId']

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

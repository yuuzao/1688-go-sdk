# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class ComAlibabaCbuOfferQualityAdviceQueryListParam(BaseApi):
    """（修改商品场景）根据商品id列表获取质量星级优化建议

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=com.alibaba.cbu.offer.quality.advice.queryList&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productIDs = None

    def get_api_uri(self):
        return '1/com.alibaba.product/com.alibaba.cbu.offer.quality.advice.queryList'

    def get_required_params(self):
        return ['productIDs']

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

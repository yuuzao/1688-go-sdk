# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductRecommendQueryProductListByGroupIdParam(BaseApi):
    """ 根据groupId获取商品列表

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.recommend.queryProductListByGroupId&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.groupId = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.recommend.queryProductListByGroupId'

    def get_required_params(self):
        return ['groupId']

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

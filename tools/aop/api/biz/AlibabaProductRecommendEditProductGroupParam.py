# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductRecommendEditProductGroupParam(BaseApi):
    """修改商家热推分组信息

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.recommend.editProductGroup&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productPromoteOperationParam = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.recommend.editProductGroup'

    def get_required_params(self):
        return ['productPromoteOperationParam']

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

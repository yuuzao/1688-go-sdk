# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class ProductAsyncQueryInfoGetInfoParam(BaseApi):
    """商品发布异步信息查询，包含品牌数据查询，类目推荐、标题推荐等。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=product.asyncQueryInfo.getInfo&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.optType = None
        self.dataJson = None

    def get_api_uri(self):
        return '1/com.alibaba.product/product.asyncQueryInfo.getInfo'

    def get_required_params(self):
        return ['optType', 'dataJson']

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

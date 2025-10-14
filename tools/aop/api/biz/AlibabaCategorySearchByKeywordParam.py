# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaCategorySearchByKeywordParam(BaseApi):
    """根据关键字搜索发布类目，发布类目都是叶子类目

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.category.searchByKeyword&v=1&cat=aop.category

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.keyword = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.category.searchByKeyword'

    def get_required_params(self):
        return ['keyword']

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

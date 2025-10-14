# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class RelativeCategoryListParam(BaseApi):
    """无参数时获取一级类目和关联进行类目的数据列表，传入一级类目获取指定一级类目和关联经营类目的数据列表。


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.cateId = None

    def get_api_uri(self):
        return '1/com.alibaba.product/relative.category.list'

    def get_required_params(self):
        return ['cateId']

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

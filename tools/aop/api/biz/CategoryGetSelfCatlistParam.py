# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class CategoryGetSelfCatlistParam(BaseApi):
    """获取指定会员（供应商）的自定义商品分类信息

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=category.getSelfCatlist&v=1&cat=userCategory

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.memberId = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/category.getSelfCatlist'

    def get_required_params(self):
        return ['memberId']

    def get_multipart_params(self):
        return []

    def need_sign(self):
        return True

    def need_timestamp(self):
        return False

    def need_auth(self):
        return False

    def need_https(self):
        return False

    def is_inner_api(self):
        return False

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class UserCategoryOffersRemoveParam(BaseApi):
    """批量移除自定义分类下的商品，一次最多操作50个商品

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=userCategory.offers.remove&v=1&cat=userCategory

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.offerIds = None
        self.categoryId = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/userCategory.offers.remove'

    def get_required_params(self):
        return ['offerIds', 'categoryId']

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

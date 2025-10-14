# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class UserCategoryGetOfferIdsParam(BaseApi):
    """本接口实现通过数据接口的形式，批量获取指定产品所属的自定义分类ID

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=userCategory.get.offerIds&v=1&cat=userCategory

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.offerIds = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/userCategory.get.offerIds'

    def get_required_params(self):
        return ['offerIds']

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

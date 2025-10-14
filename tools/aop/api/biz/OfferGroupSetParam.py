# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class OfferGroupSetParam(BaseApi):
    """阿里巴巴中国网站会员开启或关闭自定义分类功能

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=offerGroup.set&v=1&cat=userCategory

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.switchType = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/offerGroup.set'

    def get_required_params(self):
        return ['switchType']

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

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AppExpireGetParam(BaseApi):
    """ISV获取自己名下的应用最近一个月的到期的订单信息列表。
只会状态是服务中或者待发布的才有到期时间

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=app.expire.get&v=1&cat=aop.service

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.gmtServiceEnd = None
        self.memberId = None
        self.bizStatusList = None
        self.pageSize = None
        self.startIndex = None
        self.loginId = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/app.expire.get'

    def get_required_params(self):
        return ['gmtServiceEnd', 'memberId', 'bizStatusList', 'pageSize', 'startIndex', 'loginId']

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

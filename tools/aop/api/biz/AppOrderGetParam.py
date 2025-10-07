# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AppOrderGetParam(BaseApi):
    """获取调用该api的app在服务市场被订购的订单列表。appkey唯一表示一个app

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=app.order.get&v=1&cat=service

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.gmtCreate = None
        self.memberId = None
        self.bizStatusList = None
        self.pageSize = None
        self.startIndex = None
        self.loginId = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/app.order.get'

    def get_required_params(self):
        return ['gmtCreate', 'memberId', 'bizStatusList', 'pageSize', 'startIndex', 'loginId']

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

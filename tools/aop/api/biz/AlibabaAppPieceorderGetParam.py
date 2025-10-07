# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaAppPieceorderGetParam(BaseApi):
    """订购的订单列表

    References
    ----------
    https://open.1688.com/api/api.htm?ns=cn.alibaba.open&n=alibaba.app.pieceorder.get&v=1&cat=service

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.startIndex = None
        self.gmtCreate = None
        self.aliId = None
        self.pageSize = None
        self.bizStatusList = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/alibaba.app.pieceorder.get'

    def get_required_params(self):
        return ['startIndex', 'gmtCreate', 'aliId', 'pageSize', 'bizStatusList']

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

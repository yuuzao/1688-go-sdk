# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class DisplayOrderAttributesGetListParam(BaseApi):
    """用户订单筛选的订单标信息查询接口

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=display.orderAttributes.getList&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)

    def get_api_uri(self):
        return '1/com.alibaba.trade/display.orderAttributes.getList'

    def get_required_params(self):
        return []

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

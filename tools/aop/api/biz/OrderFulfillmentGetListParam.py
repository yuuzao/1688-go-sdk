# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class OrderFulfillmentGetListParam(BaseApi):
    """获取用户的履约相关数据

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=order.fulfillment.getList&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.fulfillmentMemberRequest = None

    def get_api_uri(self):
        return '1/com.alibaba.trade/order.fulfillment.getList'

    def get_required_params(self):
        return ['fulfillmentMemberRequest']

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

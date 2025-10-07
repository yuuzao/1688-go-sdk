# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaTradeOrderPostponeConfirmTimeParam(BaseApi):
    """延迟订单确认时间。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=alibaba.trade.order.PostponeConfirmTime&v=1&cat=aop.trade

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.orderId = None
        self.subPayOrderId = None
        self.delayedDays = None

    def get_api_uri(self):
        return '1/com.alibaba.trade/alibaba.trade.order.PostponeConfirmTime'

    def get_required_params(self):
        return ['orderId', 'subPayOrderId', 'delayedDays']

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

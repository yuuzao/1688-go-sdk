# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaTradeRefundQueryOrderRefundListParam(BaseApi):
    """根据订单号或退款单列表查询退款单列表，有可能有延迟。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=alibaba.trade.refund.queryOrderRefundList&v=1&cat=order_refund

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.orderId = None
        self.applyStartTime = None
        self.applyEndTime = None
        self.refundStatusSet = None
        self.buyerMemberId = None
        self.buyerLoginId = None
        self.currentPageNum = None
        self.pageSize = None
        self.logisticsNo = None
        self.modifyStartTime = None
        self.modifyEndTime = None
        self.dipsuteType = None

    def get_api_uri(self):
        return '1/com.alibaba.trade/alibaba.trade.refund.queryOrderRefundList'

    def get_required_params(self):
        return ['orderId', 'applyStartTime', 'applyEndTime', 'refundStatusSet', 'buyerMemberId', 'buyerLoginId', 'currentPageNum', 'pageSize', 'logisticsNo', 'modifyStartTime', 'modifyEndTime', 'dipsuteType']

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

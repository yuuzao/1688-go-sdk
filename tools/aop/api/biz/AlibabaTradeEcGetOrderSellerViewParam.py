# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaTradeEcGetOrderSellerViewParam(BaseApi):
    """获取单个交易明细信息，仅限卖家调用

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=alibaba.trade.ec.getOrder.sellerView&v=1&cat=aop.trade

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.orderId = None
        self.includeFields = None
        self.needOutChannel = None
        self.needSendGoodsOverdueRisk = None
        self.needDeliverGoodsOverdueRisk = None

    def get_api_uri(self):
        return '1/com.alibaba.trade/alibaba.trade.ec.getOrder.sellerView'

    def get_required_params(self):
        return ['orderId', 'includeFields', 'needOutChannel', 'needSendGoodsOverdueRisk', 'needDeliverGoodsOverdueRisk']

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

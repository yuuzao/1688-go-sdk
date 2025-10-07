# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaInvoiceDecryptParam(BaseApi):
    """根据授权用户订单号获取发票信息

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.trade&n=alibaba.invoice.decrypt&v=1&cat=trade

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.orderId = None

    def get_api_uri(self):
        return '1/com.alibaba.trade/alibaba.invoice.decrypt'

    def get_required_params(self):
        return ['orderId']

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

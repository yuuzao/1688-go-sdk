# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaLogisticsOfficialPickupParam(BaseApi):
    """1688大市场订单，官方物流提货，支持主单发货；暂不支持合并发货以及子单维度多次发货。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.logistics&n=alibaba.logistics.officialPickup&v=1&cat=aop.logistics

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.sendGoods = None
        self.remarks = None
        self.gmtSend = None

    def get_api_uri(self):
        return '1/com.alibaba.logistics/alibaba.logistics.officialPickup'

    def get_required_params(self):
        return ['sendGoods', 'remarks', 'gmtSend']

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

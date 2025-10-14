# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaLogisticsFreightTemplateOperateCheckParam(BaseApi):
    """官方物流模板，目前只有特定的发货地址支持官方物流模板。需要通过该接口，在新发商品和编辑商品过程中，对官方物流模板的支撑情况做预判校验。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.logistics&n=alibaba.logistics.freightTemplate.operate.check&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.addressId = None
        self.categoryId = None
        self.originTemplateId = None
        self.targetTemplateId = None

    def get_api_uri(self):
        return '1/com.alibaba.logistics/alibaba.logistics.freightTemplate.operate.check'

    def get_required_params(self):
        return ['addressId', 'categoryId', 'originTemplateId', 'targetTemplateId']

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

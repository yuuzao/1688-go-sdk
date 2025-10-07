# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductModifyStockParam(BaseApi):
    """修改产品库存该接口支持增量修改和全量修改，通过入参控制，默认为增量修改

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.modifyStock&v=1&cat=product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productStockChange = None
        self.webSite = None
        self.increaceModify = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.modifyStock'

    def get_required_params(self):
        return ['productStockChange', 'webSite', 'increaceModify']

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

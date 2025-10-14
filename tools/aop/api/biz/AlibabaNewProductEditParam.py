# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaNewProductEditParam(BaseApi):
    """新版商品编辑

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.new.product.edit&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.catId = None
        self.offerId = None
        self.scene = None
        self.dataBody = None
        self.bizParam = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.new.product.edit'

    def get_required_params(self):
        return ['catId', 'offerId', 'scene', 'dataBody', 'bizParam']

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

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaNewProductAddParam(BaseApi):
    """新版商品发布

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.new.product.add&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.catId = None
        self.scene = None
        self.dataBody = None
        self.bizParam = None
        self.productSourceChannels = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.new.product.add'

    def get_required_params(self):
        return ['catId', 'scene', 'dataBody', 'bizParam', 'productSourceChannels']

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

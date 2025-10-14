# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaNewProductGetSubSchemaParam(BaseApi):
    """当商品发布组件中的supportLevelProp属性为true时，可以通过该接口来获取商品发布级联子组件规则。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.new.product.getSubSchema&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.catId = None
        self.scene = None
        self.dataBody = None
        self.bizParam = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.new.product.getSubSchema'

    def get_required_params(self):
        return ['catId', 'scene', 'dataBody', 'bizParam']

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

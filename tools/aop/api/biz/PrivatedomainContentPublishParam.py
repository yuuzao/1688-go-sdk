# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class PrivatedomainContentPublishParam(BaseApi):
    """1688内容发布，可以通过该接口发布1688内容信息


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.contentGeneratorParam = None

    def get_api_uri(self):
        return '1/com.alibaba.multimedia/privatedomain.content.publish'

    def get_required_params(self):
        return ['contentGeneratorParam']

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

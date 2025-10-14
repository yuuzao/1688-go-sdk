# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AppUserTraceUploadParam(BaseApi):
    """轻应用数据回传


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.bizTs = None
        self.bizKey = None
        self.bizData = None
        self.jumpFunction = None

    def get_api_uri(self):
        return '1/cn.alibaba.open/app.userTrace.upload'

    def get_required_params(self):
        return ['bizTs', 'bizKey', 'bizData', 'jumpFunction']

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

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class CarriagecenterVoucherBySellerUploadParam(BaseApi):
    """发货凭证上传


    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.apiOrderId = None
        self.apiBase64 = None
        self.apiFileType = None

    def get_api_uri(self):
        return '1/com.alibaba.logistics/carriagecenter.voucherBySeller.upload'

    def get_required_params(self):
        return ['apiOrderId', 'apiBase64', 'apiFileType']

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

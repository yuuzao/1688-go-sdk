# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class BatchLoginidOpenuidEncryptParam(BaseApi):
    """用户LoginId批量加密转换为Openuid接口

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.account&n=batch.loginid.openuid.encrypt&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.input = None

    def get_api_uri(self):
        return '1/com.alibaba.account/batch.loginid.openuid.encrypt'

    def get_required_params(self):
        return ['input']

    def get_multipart_params(self):
        return []

    def need_sign(self):
        return True

    def need_timestamp(self):
        return True

    def need_auth(self):
        return True

    def need_https(self):
        return False

    def is_inner_api(self):
        return False

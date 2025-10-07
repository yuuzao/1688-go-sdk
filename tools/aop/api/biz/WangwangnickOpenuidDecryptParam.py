# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class WangwangnickOpenuidDecryptParam(BaseApi):
    """Openuid转换解密为旺旺昵称接口。该接口进行风控，仅可使用于用户需要唤起旺旺，不允许自动化批量操作，不允许作为解密接口将明文展示给用户。旺旺支持加密后回收，请勿使用于其他场景。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.account&n=wangwangnick.openuid.decrypt&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.openUid = None

    def get_api_uri(self):
        return '1/com.alibaba.account/wangwangnick.openuid.decrypt'

    def get_required_params(self):
        return ['openUid']

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

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class LoginidOpenuidEncryptParam(BaseApi):
    """用户loginId加密转换为Openuid接口。该接口进行风控，不允许批量操作，仅允许商家手动触发，比如：搜索用户订单、设置规则等功能

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.account&n=loginid.openuid.encrypt&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.loginId = None

    def get_api_uri(self):
        return '1/com.alibaba.account/loginid.openuid.encrypt'

    def get_required_params(self):
        return ['loginId']

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

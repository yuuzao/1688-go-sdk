# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaPhotobankAlbumAddParam(BaseApi):
    """创建相册，

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.photobank.album.add&v=1&cat=aop.ibank

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.name = None
        self.description = None
        self.authority = None
        self.password = None
        self.webSite = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.photobank.album.add'

    def get_required_params(self):
        return ['name', 'description', 'authority', 'password', 'webSite']

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

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaPhotobankAlbumGetListParam(BaseApi):
    """获取相册列表

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.photobank.album.getList&v=1&cat=ibank

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.webSite = None
        self.albumType = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.photobank.album.getList'

    def get_required_params(self):
        return ['webSite', 'albumType']

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

# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaPhotobankAlbumDeleteParam(BaseApi):
    """删除相册

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.photobank.album.delete&v=1&cat=ibank

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.albumID = None
        self.webSite = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.photobank.album.delete'

    def get_required_params(self):
        return ['albumID', 'webSite']

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

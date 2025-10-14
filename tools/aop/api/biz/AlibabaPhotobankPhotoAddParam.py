# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaPhotobankPhotoAddParam(BaseApi):
    """选择的图片单张大小不超过2MB，支持jpg,jpeg,gif,bmp,png。其中不支持png图片透明色，透明处理后可能为白色或黑色。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.photobank.photo.add&v=1&cat=aop.window

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.albumID = None
        self.name = None
        self.description = None
        self.drawTxt = None
        self.imageBytes = None
        self.webSite = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.photobank.photo.add'

    def get_required_params(self):
        return ['albumID', 'name', 'description', 'drawTxt', 'imageBytes', 'webSite']

    def get_multipart_params(self):
        return ['imageBytes']

    def need_sign(self):
        return False

    def need_timestamp(self):
        return False

    def need_auth(self):
        return True

    def need_https(self):
        return False

    def is_inner_api(self):
        return False

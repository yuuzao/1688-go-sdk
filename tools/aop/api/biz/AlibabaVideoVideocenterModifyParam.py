# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaVideoVideocenterModifyParam(BaseApi):
    """修改视频中心视频

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.multimedia&n=alibaba.video.videocenter.modify&v=1&cat=video.center

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.videoId = None
        self.name = None
        self.description = None

    def get_api_uri(self):
        return '1/com.alibaba.multimedia/alibaba.video.videocenter.modify'

    def get_required_params(self):
        return ['videoId', 'name', 'description']

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

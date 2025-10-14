# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaVideoVideocenterGetParam(BaseApi):
    """获取单个视频

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.multimedia&n=alibaba.video.videocenter.get&v=1&cat=video.center

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.videoId = None

    def get_api_uri(self):
        return '1/com.alibaba.multimedia/alibaba.video.videocenter.get'

    def get_required_params(self):
        return ['videoId']

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

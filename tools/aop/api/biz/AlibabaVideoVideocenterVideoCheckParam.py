# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaVideoVideocenterVideoCheckParam(BaseApi):
    """视频制作检测，目前只有视频制作后上传到1688店铺时有数量的限制。
同时保持扩展兼容，扩展其他相关服务的限制。
当前api只兼容了work工作台中视频类型的旺铺视频，其他类型的视频本api不支持。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.multimedia&n=alibaba.video.videocenter.videoCheck&v=1&cat=video.center

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None

    def get_api_uri(self):
        return '1/com.alibaba.multimedia/alibaba.video.videocenter.videoCheck'

    def get_required_params(self):
        return []

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

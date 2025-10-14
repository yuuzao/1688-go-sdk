# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaVideoVideocenterAttachParam(BaseApi):
    """将视频中心的一个视频关联到一个1688商品，同时会设置到商品主图视频和商品详情视频，商品上传后如果立即调用该API绑定视频会导致商品写入锁抢占失败，进而导致商品绑定视频失败，因此使用时要在商品上传完成后再调用。

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.multimedia&n=alibaba.video.videocenter.attach&v=1&cat=video.center

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.productId = None
        self.location = None
        self.videoId = None

    def get_api_uri(self):
        return '1/com.alibaba.multimedia/alibaba.video.videocenter.attach'

    def get_required_params(self):
        return ['productId', 'location', 'videoId']

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

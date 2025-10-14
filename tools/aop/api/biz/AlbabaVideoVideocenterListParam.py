# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlbabaVideoVideocenterListParam(BaseApi):
    """分页查询获取用户视频中心的视频列表，默认返回第一页，每一页十条记录

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.multimedia&n=albaba.video.videocenter.list&v=1&cat=video.center

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.page = None
        self.pageSize = None

    def get_api_uri(self):
        return '1/com.alibaba.multimedia/albaba.video.videocenter.list'

    def get_required_params(self):
        return ['page', 'pageSize']

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

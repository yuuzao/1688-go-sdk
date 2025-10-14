# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaMemberBrandQueryParam(BaseApi):
    """针对实力商家，1688平台上有授权的品牌信息，商家发布商品时只能选择有授权的品牌；
通过指定商品叶子类目，查询该类目下绑定的的授权品牌列表信息，如果没有授权，返回信息为空

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.member&n=alibaba.member.brand.query&v=1&cat=

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.leafCatIds = None

    def get_api_uri(self):
        return '1/com.alibaba.member/alibaba.member.brand.query'

    def get_required_params(self):
        return ['leafCatIds']

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

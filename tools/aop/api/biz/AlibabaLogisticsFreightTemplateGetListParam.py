# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaLogisticsFreightTemplateGetListParam(BaseApi):
    """获取运费模板列表。1688有两类特殊运费模板，不在此接口返回：不传运费模板表示使用运费说明；传入1表示卖家承担运费

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.logistics&n=alibaba.logistics.freightTemplate.getList&v=1&cat=wuliu

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.webSite = None
        self.categoryId = None
        self.addressId = None

    def get_api_uri(self):
        return '1/com.alibaba.logistics/alibaba.logistics.freightTemplate.getList'

    def get_required_params(self):
        return ['webSite', 'categoryId', 'addressId']

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

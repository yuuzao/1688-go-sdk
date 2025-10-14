# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaUserDefineCategoryAddParam(BaseApi):
    """在1688中文中，创建用户的自定义类目。如果是一级类目，父类目Id传值0。如果是子类目，父类目传上一级类目的id。创建成功的话，会返回新的类目的id

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.userDefine.category.add&v=1&cat=category

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.groupName = None
        self.parentID = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.userDefine.category.add'

    def get_required_params(self):
        return ['groupName', 'parentID']

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

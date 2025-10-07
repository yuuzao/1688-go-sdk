# -*- coding: utf-8 -*-
from aop.api.base import BaseApi

class AlibabaProductListGetParam(BaseApi):
    """卖家根据条件分页查询商品列表信息。目前无法查询简易商品。如需遍历所有商品是只能使用ID排序

    References
    ----------
    https://open.1688.com/api/api.htm?ns=com.alibaba.product&n=alibaba.product.list.get&v=1&cat=aop.product

    """

    def __init__(self, domain=None):
        BaseApi.__init__(self, domain)
        self.access_token = None
        self.signs = None
        self.pageNo = None
        self.pageSize = None
        self.statusList = None
        self.categoryId = None
        self.startModifyTime = None
        self.endModifyTime = None
        self.subjectKey = None
        self.cargoNumber = None
        self.productIds = None
        self.beginStar = None
        self.endStar = None
        self.groupIds = None
        self.startPublishTime = None
        self.endPublishTime = None
        self.startExpiredTime = None
        self.endExpiredTime = None
        self.priceStart = None
        self.priceEnd = None
        self.orderByCondition = None
        self.orderByType = None
        self.supportOnlineTrade = None
        self.privateOffer = None
        self.needDetail = None
        self.needFreight = None
        self.needUserCategoryInfo = None

    def get_api_uri(self):
        return '1/com.alibaba.product/alibaba.product.list.get'

    def get_required_params(self):
        return ['signs', 'pageNo', 'pageSize', 'statusList', 'categoryId', 'startModifyTime', 'endModifyTime', 'subjectKey', 'cargoNumber', 'productIds', 'beginStar', 'endStar', 'groupIds', 'startPublishTime', 'endPublishTime', 'startExpiredTime', 'endExpiredTime', 'priceStart', 'priceEnd', 'orderByCondition', 'orderByType', 'supportOnlineTrade', 'privateOffer', 'needDetail', 'needFreight', 'needUserCategoryInfo']

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

# -*- coding: utf-8 -*-
"""
@Author: xiaohao
@Date: 2019/9/4
"""
from django.urls import path
from . import views

urlpatterns = [
    # 测试路由规则 hehe/ hehehe/
    path("hehe", views.hehe),
    path("hehehe", views.hehehe),
]

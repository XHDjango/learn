# -*- coding: utf-8 -*-
'''
@Author: xiaohao
@Date: 2019/9/4
'''
from django.urls import path, re_path

from . import views

app_name = "learn_view"
urlpatterns = [
    # 测试路由规则 hehe/ hehehe/  (从上到下进行最优匹配)
    path('hehe/', views.hehe),
    re_path(r'^hehehe/', views.hehehe),

    path('grade/', views.grade),
    path('grade/<int:grade_id>', views.student, name="student"),

    path('blog_md/', views.BlogMDModelForm.as_view(), name="blog_md"),
]

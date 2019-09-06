# -*- coding: utf-8 -*-
"""
@Author: xiaohao
@Date: 2019/9/6
"""

from django.urls import path
from . import views

app_name = "learn_model"
urlpatterns = [
    path("bind", views.bind, name="bind"),
]

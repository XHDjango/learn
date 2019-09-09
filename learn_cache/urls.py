# -*- coding: utf-8 -*-
"""
@Author: xiaohao
@Date: 2019/9/9
"""
from django.urls import path
from . import views

app_name = "learn_cache"
urlpatterns = [
    path("news", views.news, name="news"),
    path("my_news", views.my_news, name="my_news"),
]

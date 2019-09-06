# -*- coding: utf-8 -*-
"""
@Author: xiaohao
@Date: 2019/9/6
"""

from django.urls import path
from . import views

app_name = "learn_model"
urlpatterns = [
    path("new_person", views.new_person, name="new_person"),
    path("person_info", views.show_person_info, name="person_info"),
    path("del_person/<int:person_id>", views.del_person, name="del_person"),
    path("del_idcard/<int:id_num>", views.del_idcard, name="del_idcard"),
]

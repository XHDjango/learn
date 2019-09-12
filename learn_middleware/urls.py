# -*- coding:utf-8 -*-
'''
@Author: lamborghini1993
@Date: 2019-09-11 14:51:15
@UpdateDate: 2019-09-11 15:11:05
@Description: 
'''
from django.urls import path
from . import views

app_name = "learn_middleware"
urlpatterns = [
    path("static", views.static, name="static"),
    path("anti_scrapy", views.anti_scrapy, name="anti_scrapy"),

    path("add_student",views.add_student,name="add_student"),
    path("get_student",views.get_student,name="get_student"),
]

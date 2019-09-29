# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2019-09-24 17:08:50
@Description: 
"""

from django.urls import path
from . import views

name = "learn_form"
urlpatterns = [
    path("", views.index, name="index"),
]

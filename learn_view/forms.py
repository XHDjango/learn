# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2019-09-12 14:57:40
@Description:表单
"""

from django import forms
from mdeditor.fields import MDTextFormField
from .models import BlogMDModel


class BlogMDForm(forms.Form):
    title = forms.CharField()
    content = MDTextFormField(config_name="custom")


class BlogMDModleForm(forms.ModelForm):
    class Meta:
        model = BlogMDModel
        fields = "__all__"

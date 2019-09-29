# -*- coding: utf-8 -*-
"""
@Author: lamborghini1993
@Date: 2019-09-24 17:11:31
@Description: 表单模块
"""

from django.forms import Form, widgets, fields


class MyForm(Form):
    user = fields.CharField(
        widget=widgets.Textarea()
        # widget=widgets.TextInput(attrs={"id": "il", "class": "cl"})
    )
    gender = fields.ChoiceField(
        choices=(
            (1, "男"),
            (2, "女")
        ),
        initial=2,
        widget=widgets.RadioSelect
    )

    city = fields.CharField(
        initial=2,
        widget=widgets.Select(choices=((1, '上海'), (2, '北京'),))
    )

    pwd = fields.CharField(
        widget=widgets.PasswordInput(attrs={"class": "cl"}, render_value=True)
    )

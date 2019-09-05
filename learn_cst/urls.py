from django.urls import path
from . import views

app_name = "cst"
urlpatterns = [
    path('c_user', views.cookie_user, name="c_user"),
    path('c_login', views.cookie_login, name="c_login"),
    path('c_logout', views.cookie_logout, name="c_logout"),

    path('s_user', views.session_user, name="s_user"),
    path('s_login', views.session_login, name="s_login"),
    path('s_logout', views.session_logout, name="s_logout"),
]

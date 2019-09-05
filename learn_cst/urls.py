from django.urls import path
from . import views

app_name = "cst"
urlpatterns = [
    path('c_login', views.cookie_login, name="login"),
    path('c_logout', views.cookie_logout, name="logout"),
    path('user', views.user, name="user"),
]

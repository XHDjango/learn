from django.shortcuts import render, redirect
from django.urls import reverse

COOKIE_KEYNAME = "name"


def user(request):
    username = request.COOKIES.get(COOKIE_KEYNAME)
    if username:
        return render(request, "user.html", context=locals())
    return redirect(reverse("cst:login"))


def cookie_login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username: str = request.POST.get("username")
    response = redirect(reverse("cst:user"))
    # response.set_signed_cookie(COOKIE_KEYNAME, username, "salt")  # 加salt的cookie
    response.set_cookie(COOKIE_KEYNAME, username)
    return response


def cookie_logout(request):
    # 删除服务器cookie是错误的
    # request.COOKIES.pop(COOKIE_KEYNAME)

    # 删除浏览器的cookie
    response = redirect(reverse("cst:login"))
    response.delete_cookie(COOKIE_KEYNAME)
    return response

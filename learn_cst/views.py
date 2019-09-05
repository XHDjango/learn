from django.shortcuts import render, redirect
from django.urls import reverse

COOKIE_KEYNAME = "c_name"
SESSION_KEYNAME = "s_name"


def cookie_user(request):
    # request.get_signed_cookie(COOKIE_KEYNAME, salt="salt")
    username = request.COOKIES.get(COOKIE_KEYNAME)
    if username:
        return render(request, "c_user.html", context=locals())
    return redirect(reverse("cst:c_login"))


def cookie_login(request):
    if request.method == "GET":
        return render(request, "c_login.html")
    username: str = request.POST.get("username")
    response = redirect(reverse("cst:c_user"))
    # response.set_signed_cookie(COOKIE_KEYNAME, username, "salt")  # 加salt的cookie
    response.set_cookie(COOKIE_KEYNAME, username)
    return response


def cookie_logout(request):
    # 删除服务器cookie是错误的
    # request.COOKIES.pop(COOKIE_KEYNAME)

    # 删除浏览器的cookie
    response = redirect(reverse("cst:c_login"))
    response.delete_cookie(COOKIE_KEYNAME)
    return response


# def session_login(request):
#     if request.method == "GET":
#         return render(request, "s_login.html")
#     username: str = request.POST.get("username")
#     request.session[SESSION_KEYNAME] = username
#     return redirect(reverse("cst:s_user"))


# def session_logout(request):
#     return None


# def session_user(request):
#     return None
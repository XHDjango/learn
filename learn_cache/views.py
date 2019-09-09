import time

from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page


@cache_page(30)
def news(request):
    lst = ["这是第%s个大新闻" % i for i in range(1, 10)]
    time.sleep(5)
    return render(request, "news.html", context={"news": lst})


def my_news(request):
    cache_key = "mynews"
    mynew = cache.get(cache_key)
    if mynew:
        return HttpResponse(mynew)
    lst = ["这是第%s个大新闻" % i for i in range(1, 10)]
    time.sleep(5)
    mynew = render(request, "news.html", context={"news": lst})
    cache.set(cache_key, mynew, 30)
    return mynew

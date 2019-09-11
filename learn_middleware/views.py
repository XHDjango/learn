from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def static(request):
    return HttpResponse("static")


def anti_scrapy(request):
    return HttpResponse("scrapy 成功")

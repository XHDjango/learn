from django.shortcuts import render
from django.http import HttpResponse


def hehe(request):
    return HttpResponse("hehe")


def hehehe(request):
    return HttpResponse("hehehe")

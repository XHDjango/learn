from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Student


# Create your views here.
def static(request):
    return HttpResponse("static")


def anti_scrapy(request):
    return HttpResponse("scrapy 成功")


def add_student(request):
    for x in range(1000):
        Student.objects.create(name="love%s" % x, age=x)
    return HttpResponse("创建成功")


def get_student(request):
    students = Student.objects.all()
    per_page = int(request.GET.get("num", 10))
    paginator = Paginator(students, per_page)
    page_index = int(request.GET.get("page", 1))
    if page_index < 1:
        page_index = 1
    if page_index > paginator.num_pages:
        page_index = paginator.num_pages

    index = page_index
    page_list = [index]
    i = 1
    while len(page_list) < 5:
        temp = index - i
        if temp > 0:
            page_list.insert(0, temp)
        temp = index + i
        if temp < paginator.num_pages:
            page_list.append(temp)
        i += 1

    data = {
        "page": paginator.get_page(page_index),
        "page_list": page_list,
    }
    return render(request, "students.html", context=data)

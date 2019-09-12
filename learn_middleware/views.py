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
    page = int(request.GET.get("page", 1))
    print("info:", per_page, page)
    paginator = Paginator(students, per_page)
    data = {
        "page": paginator.get_page(page),
        "page_list": paginator.page_range,
    }
    return render(request, "students.html", context=data)

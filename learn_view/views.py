from django.http import HttpResponse
from django.shortcuts import render

from learn_view.models import Grade
from learn_view.models import Student


def hehe(request):
    return HttpResponse("hehe")


def hehehe(request):
    return HttpResponse("hehehe")


def grade(request):
    grade_list = Grade.objects.all()
    return render(request, "learn_view/grade.html", context=locals())


def student(request, grade_id):
    student_list = Student.objects.filter(grade=grade_id)
    return render(request, "learn_view/student.html", context=locals())

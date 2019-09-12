from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

from learn_view.models import Grade
from learn_view.models import Student
from . import forms
from django.views import generic


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


class BlogMDModelForm(generic.CreateView):
    form_class = forms.BlogMDModleForm
    template_name = "blog_md.html"

    def get_success_url(self):
        return reverse("learn_view:blog_md")

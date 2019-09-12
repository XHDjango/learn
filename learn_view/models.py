from django.db import models
from mdeditor.fields import MDTextField


class Grade(models.Model):
    name = models.CharField(max_length=16)


class Student(models.Model):
    name = models.CharField(max_length=16)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class BlogMDModel(models.Model):
    title = models.CharField(max_length=128)
    content = MDTextField()

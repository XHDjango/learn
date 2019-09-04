from django.db import models


class Grade(models.Model):
    name = models.CharField(max_length=16)


class Student(models.Model):
    name = models.CharField(max_length=16)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

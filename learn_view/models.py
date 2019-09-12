from django.db import models
from mdeditor.fields import MDTextField


class Grade(models.Model):
    name = models.CharField(max_length=16)


class Student(models.Model):
    name = models.CharField(max_length=16)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class BlogMDModel(models.Model):
    title = models.CharField(max_length=128,verbose_name="标题")
    content = MDTextField(verbose_name="内容")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

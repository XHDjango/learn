from django.conf import settings
from django.contrib import auth
from django.db import models


class MySpecialUser(models.Model):
    user = models.OneToOneField(
        auth.get_user_model(),
        on_delete=models.CASCADE,
    )
    supervisor = models.OneToOneField(
        auth.get_user_model(),
        on_delete=models.CASCADE,
        related_name='supervisor_of',
    )


class Person(models.Model):
    name = models.CharField(max_length=16)


class IDCard(models.Model):
    id_num = models.IntegerField(primary_key=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)


class Car(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        abstract = True


class Lamborghini(Car):
    price = models.IntegerField()


class UserInfo(models.Model):
    name = models.CharField(max_length=16)
    image = models.ImageField(upload_to="icon")

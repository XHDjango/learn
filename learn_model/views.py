from django.shortcuts import render, redirect
from .models import Person, IDCard
from django.urls import reverse


def new_person(request):
    if request.method == "GET":
        return render(request, "new_person.html")
    username = request.POST.get("username")
    idcard = request.POST.get("idcard")
    oPerson = Person.objects.create(name=username)
    IDCard.objects.create(id_num=idcard, person_id=oPerson.id)
    return redirect(reverse("learn_model:person_info"))


def show_person_info(request):
    data = {
        "persons": Person.objects.all(),
        "idcards": IDCard.objects.all(),
    }
    return render(request, "show_person_info.html", context=data)


def del_person(request, person_id):
    oPerson = Person.objects.get(pk=person_id)
    oPerson.delete()
    return redirect(reverse("learn_model:person_info"))


def del_idcard(request, id_num):
    oIDCard = IDCard.objects.get(id_num=id_num)
    oIDCard.delete()
    return redirect(reverse("learn_model:person_info"))

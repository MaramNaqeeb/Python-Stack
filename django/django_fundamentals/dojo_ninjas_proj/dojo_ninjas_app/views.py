from django.shortcuts import render, redirect
from .models import Dojo, Ninja

# Create your views here.


def form(request):
    context = {
        "all_the_dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)


def one(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect("/")


def many(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo=Dojo.objects.get(id=int(request.POST['dojo'])),
    )

    return redirect("/")

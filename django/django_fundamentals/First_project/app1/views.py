
from django.shortcuts import  redirect,HttpResponse 

def root_method(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/root")

def show(request, number):
    print(number)
    return HttpResponse("placeholder to display blog number " +number)

def edit(request, number):
    print(number)
    return HttpResponse("placeholder to edit blog number" +number)

def destroy(request, number):
    return redirect ("/blogs")
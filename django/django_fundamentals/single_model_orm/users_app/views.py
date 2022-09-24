from django.shortcuts import render,redirect
from .models import User


    
def form(request):
    return render(request,"form.html")

def create(request):
    User.objects.create(first_name=request.POST["firstname"], last_name=request.POST["lastname"],email_address=request.POST["email"],age=request.POST["age"])
    return redirect("/show")

    
def show(request):
    context = {
    	"all_the_users": User.objects.all()
    }
    return render(request,"show.html",context)
     















import logging
from django.shortcuts import redirect,render
from django.contrib import messages
from .models import User
import bcrypt


def root(request):

    return render(request,"login.html")


def add_user(request):
        errors = User.objects.validate_user(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # else:
        # user=User.objects.get(id=id)
      
        password=request.POST['password']        
        password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=password_hash,
            )
        return redirect("/wall")

def log_user(request):
    
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session["name"] = logged_user.first_name
            return redirect('/wall/'+str(logged_user.id))
    return redirect("/")




def clear(request):
    #request.session.clear()
    del request.session['userid']
    del request.session['name']
    return redirect('/')    

# def message_login(request):
#     return render (request,'login.html')








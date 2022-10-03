from django.shortcuts import redirect,render
from django.contrib import messages
from .models import User
import re
import bcrypt


def root(request):
    context= {
        "users" : User.objects.all(),
    }
    return render(request,"reg_log.html",context)

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
                                                       
        # messages.success(request, "successfully registered")

        return redirect("/")

def log_user(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            return redirect('/success')
        return redirect("/")

def success(request):
    return render(request,'success.html')


def clear(request):
    del request.session['userid']
    return redirect('/')    


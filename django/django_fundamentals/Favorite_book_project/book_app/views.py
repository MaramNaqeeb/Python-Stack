
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import User, Book
import bcrypt


def root(request):

    return render(request, "log.html")


def add_user(request):
        errors = User.objects.validate_user(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # else:
        # user=User.objects.get(id=id)

        password = request.POST['password']
        password_hash = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=password_hash,
        )
        return redirect("/book")


def log_user(request):

    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            request.session["name"] = logged_user.first_name
            return redirect('/book')
        return redirect("/")
    return redirect("/")


def clear(request):
    del request.session['userid']
    del request.session['name']
    return redirect('/')

def add_book(request):
    errors = Book.objects.validate_book(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/book')  
    else:
        Book.objects.create(
        title=request.POST['title'],
        desc=request.POST['description'],
        uploaded_by_id = request.session['userid'],
    )
        return redirect("/book")




def book(request):
    context={
        "all_uploaded_books":Book.objects.all(),
    }
    return render(request, 'book.html',context)

def show(request,id):
    context={
        'favorite': Book.objects.get(id=id),
        'user':  User.objects.get(id= request.session['userid'])
    }
    return render(request,'details.html',context)

def edit(request,id):

    book1=Book.objects.get(id=id)
    book1.title=request.POST["title"]
    book1.desc=request.POST["description"]
    book1.save()
    
    return redirect('/book')

def destroy(request,id):
    book1=Book.objects.get(id=id)
    book1.delete()
    return redirect('/book')

def add_to_fav(request,id):
    user_likes= User.objects.get(id=request.session['userid'])
    book_liked=Book.objects.get(id=int(id))
    book_liked.users_who_like.add(user_likes)
    book_liked.save()
    return redirect('/book/'+str(id))

def un_fav(request,id):
    user_dislike= User.objects.get(id=request.session['userid'])
    book_disliked=Book.objects.get(id=int(id))
    book_disliked.users_who_like.remove(user_dislike)
    book_disliked.save()
    return redirect('/book/'+str(id))


        
        

 






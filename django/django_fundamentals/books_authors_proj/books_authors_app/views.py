from django.shortcuts import render,redirect
from .models import Book,Author


def all_the_books(request):
    context={
     'all_the_books':Book.objects.all()
    }
    return render (request,'book.html',context)

def book_create(request):
    book_title = request.POST["title"]
    book_desc = request.POST["description"]
    Book.objects.create(
        title = book_title,
        desc = book_desc
    )
    return redirect('/')

def show_book(request,id):
    book = Book.objects.get(id=id)
    context={
        'my_book': book,
        'authors':Author.objects.all()
    }
    return render(request,'show_book.html',context)

def add_author_to_book(request,id):
    author=Author.objects.get(id=request.POST['authors'])
    book = Book.objects.get(id=id)
    book.authors.add(author)
    return redirect('/book/'+str(id))



def all_authors(request):
    context={
     'all_the_authors':Author.objects.all()
    }
    return render (request,'author.html',context)

def author_create(request):
    author_first_name = request.POST["first_name"]
    author_last_name = request.POST["last_name"]
    author_notes=request.POST['notes']
    Author.objects.create(
        first_name = author_first_name,
        last_name = author_last_name,
        notes= author_notes
    )
    return redirect('/authors')
    

def show_author(request,id):
    author = Author.objects.get(id=id)
    context={
        'my_author': author,
        'books':Book.objects.all()
    }
    return render(request,'show_author.html',context)

def add_book_to_author(request,id):
    book=Book.objects.get(id=request.POST['books'])
    author = Author.objects.get(id=id)
    author.books.add(book)
    return redirect('/author/'+str(id))



    

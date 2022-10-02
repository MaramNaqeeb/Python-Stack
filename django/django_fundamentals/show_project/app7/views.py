from django.shortcuts import render,redirect
from .models import Show

def all_shows(request):
    context={
     'all_shows':Show.objects.all()
    }
    return render (request,'all_shows.html',context)

def show_submit(request,id):
   
    context={
        'my_show': Show.objects.get(id=id)
    }
    return render(request,'show_submit.html',context)


def shows_new(request):
    return render(request,'tv.html')

def show_create(request):
    show_title = request.POST['title']
    show_network = request.POST['network']
    show_release_date=request.POST['release_date']
    show_desc=request.POST['description']
    Show.objects.create(
        title = show_title,
        network=show_network,
        release_date=show_release_date,
        desc = show_desc
    )
    return redirect('/shows')


def edit(request,id):

    context={
        'edit':Show.objects.get(id=id),
    }
    return render(request,'show_edit.html',context)

def show_edit(request,id):

    showme=Show.objects.get(id=id)
    showme.title=request.POST["title"]
    showme.network=request.POST["network"]
    showme.release_date=request.POST["release_date"]
    showme.desc=request.POST["description"]
    showme.save()
    
    return redirect(f'/shows/{id}')

def destroy(request,show_id):
    show1=Show.objects.get(id=show_id)
    show1.delete()
    return redirect('/shows')



# def destroy(request):
#     del request.session['all_shows']
#     return redirect('/shows')



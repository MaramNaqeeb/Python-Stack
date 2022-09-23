from django.shortcuts import render, redirect
def root(request):
      return render(request,"registration.html")

def result(request):
   
      name_from_form = request.POST['name']
      location_from_form = request.POST['location']
      language_from_form = request.POST['language']
      comment = request.POST['comment']
    
      context={
      "name_on_template":name_from_form,
      "location_on_template":location_from_form,
      "language_on_template":language_from_form,
      "comment_on_template":comment,
      } 
      return render(request,"show.html",context)

      

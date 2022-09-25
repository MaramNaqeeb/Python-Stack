from django.shortcuts import render,redirect
import random

def root(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(0, 100)
    return render(request, 'index.html')

def determine(request):
    request.session['digit'] = request.POST['number']
    if int(request.session['number']) < int(request.session['digit']):
        request.session['status']="too high"
    
    elif   int(request.session['number']) > int(request.session['digit']):
        request.session['status']="too low"
    elif   int(request.session['number']) =='':
        del request.session['number']
    else: 
        request.session['status']="correct"
        del request.session['number']
    
    return redirect("/")



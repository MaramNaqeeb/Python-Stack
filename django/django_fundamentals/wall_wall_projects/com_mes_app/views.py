from django.shortcuts import render,redirect

# Create your views here.
from log_in_app.models import User
from .models import Message, Comment

def wall(request,id):
    if "name" not in request.session:
        return redirect("/")
    context={
        "user":User.objects.get(id=id),
        "all_messages":Message.objects.all(),
        "all_comments":Comment.objects.all(),
    }
    return render(request,'wall.html',context)
    
def message_create(request):
    print(request.POST['post_a_message'])
    print()
    Message.objects.create(message=request.POST['post_a_message'],
                        user=User.objects.get(id=request.session['userid']))
    return redirect('/wall')

def comment_create(request):
    print("*********************************"+request.POST['messageid_'])
    print("*********************************"+request.POST['post_a_comment'])
    Comment.objects.create(comment=request.POST['post_a_comment'],
                        user=User.objects.get(id=request.session['userid']),
    message=Message.objects.get(id=request.POST['messageid_']))
    return redirect('/wall/'+str(request.session['userid']))





from email.policy import default
from django.db import models

# Create your models here.
from log_in_app.models import User

class Message(models.Model):
    message=models.TextField(default='')
    user=models.ForeignKey(User,related_name='massages',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment=models.TextField(default='')
    user=models.ForeignKey(User,related_name='comments',on_delete=models.CASCADE, default=0)
    message=models.ForeignKey(Message,related_name='comments',on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)



from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validate_user(self,data):
        errors = {}
        if len(data['first_name']) < 2:
            errors['first_name_length'] = "The first name is too short"
        if len(data['last_name']) < 2:
            errors['last_name_length'] = "The last name is too short"
        if len(data['password']) < 8:
            errors['password_length'] = "The password is too short"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(data['email']):   
            errors['email'] = "Invalid email address!"
        return errors
           
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255) 
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()


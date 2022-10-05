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
 first_name = models.CharField(max_length=255)
 last_name = models.CharField(max_length=255)
 # liked_books = a list of books a given user likes
 # books_uploaded = a list of books uploaded by a given user
 email = models.EmailField(max_length=255)
 password = models.CharField(max_length=50)
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
 objects=UserManager()
 
class BookManager(models.Manager):
    def validate_book(self,data):
        errors = {}
        if len(data['title']) < 1:
            errors['title']='title ia required'
        if len(data['description']) < 5:
            errors['description']='description is too short'
        return errors

class Book(models.Model):
 title = models.CharField(max_length=255)
 uploaded_by = models.ForeignKey(User,related_name='books_uploaded',on_delete = models.CASCADE)
 users_who_like = models.ManyToManyField(User,related_name='liked_books')
 desc=models.TextField(null=True)
 created_at=models.DateTimeField(auto_now_add=True)
 updated_at=models.DateTimeField(auto_now=True)
 objects=BookManager()


 




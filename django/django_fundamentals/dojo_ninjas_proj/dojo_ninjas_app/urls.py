from django.urls import path
from . import views

urlpatterns=[
    path('one',views.one),
    path('many',views.many),
    path('',views.form),

]
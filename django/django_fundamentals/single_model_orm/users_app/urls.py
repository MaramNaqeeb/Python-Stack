from django.urls import path
from . import views
urlpatterns=[
   
    path("form",views.form),
    path("create",views.create),
    path("show",views.show),
  
    
]
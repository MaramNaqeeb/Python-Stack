from django.urls import path
from .import views
urlpatterns=[
    path('',views.root),
    path('add_user/',views.add_user),
    path('log_user',views.log_user),
    path('success',views.success),
    path('clear',views.clear),



]
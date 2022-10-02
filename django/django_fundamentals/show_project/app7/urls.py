from django.urls import path
from . import views
urlpatterns=[
    path('shows',views.all_shows),
    path('shows/new',views.shows_new),
    path('shows/<int:id>/',views.show_submit),
    path('show_create',views.show_create),
    path('shows/<int:id>/edit/',views.edit),
    path('shows/<int:id>/show_edit',views.show_edit),
    path('shows/<int:show_id>/delete/',views.destroy),
    
   
  

]
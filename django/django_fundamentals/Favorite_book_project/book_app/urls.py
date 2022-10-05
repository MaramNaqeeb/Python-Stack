from django.urls import path
from .import views
urlpatterns=[
    path('',views.root),
    path('add_user/',views.add_user),
    path('log_user',views.log_user),
    path('clear/',views.clear),
    path('add_book/',views.add_book),
    path('book',views.book),
    path('book/<int:id>',views.show),
    path('book/<int:id>/edit/',views.edit),
    path('book/<int:id>/delete/',views.destroy),
    path('add_to_fav/<int:id>', views.add_to_fav),
    path('un_fav/<int:id>', views.un_fav),
   



]
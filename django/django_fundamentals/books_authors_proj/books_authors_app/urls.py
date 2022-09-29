from django.urls import path
from . import views
urlpatterns=[
   
    path('',views.all_the_books),
    path('book_create',views.book_create),
    path('book/<int:id>', views.show_book),
    path('add_author_to_book/<int:id>',views.add_author_to_book),
    path('authors',views.all_authors),
    path('author_create',views.author_create),
    path('author/<int:id>', views.show_author),
    path('add_book_to_author/<int:id>',views.add_book_to_author),

]
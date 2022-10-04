from django.urls import path
from .import views
urlpatterns=[
    path("wall/<int:id>",views.wall),
    path('wall/message_create/',views.message_create),
    path('wall/comment_create/',views.comment_create),
]
from django.urls import path
from . import views
urlpatterns = [
    path('',views.blogHome,name="blogHome"),
    path('postcomment',views.postComment,name="postcomment"),
    path('<str:slug>/',views.blogPost,name="blogPost"),
]

# from django.contrib import admin
from django.urls import path
from books.views import get_author, post_author, post_book, get_book, update_author, patch_author, delete_author, update_book, patch_book, delete_book

urlpatterns = [
    path('get-author/',get_author ),
    path('post-author/',post_author),
    path('put-author/<id>/' , update_author),
    path('patch-author/<id>/', patch_author),
    path('delete-author/<id>/', delete_author),

    path('get-book/' ,get_book),
    path('post-book/',post_book ),
    path('update-book/<id>/', update_book),
    path('patch-book/<id>/', patch_book),
    path('delete-book/<id>/', delete_book),
]
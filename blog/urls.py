from django.urls import path
from .views import (
    BookListAPI, BookDetailAPI,
    BookUpdateAPI, BookCreateAPI, BookDeleteAPI)

urlpatterns = [
    path("list/", BookListAPI.as_view()),
    path("detail/<int:pk>/", BookDetailAPI.as_view()),
    path("edit/<int:pk>/", BookUpdateAPI.as_view()),
    path("create/", BookCreateAPI.as_view()),
    path("delete/<int:pk>/", BookDeleteAPI.as_view()),
]
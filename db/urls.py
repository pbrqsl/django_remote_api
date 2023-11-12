from django.urls import path
from db.views import pull_books_with_serializer

urlpatterns = [
    path("", pull_books_with_serializer, name="book-pull")
]

#add some code

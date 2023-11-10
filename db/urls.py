from django.urls import path
from db.views import pull_books, pull_books_with_serializer

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", pull_books_with_serializer, name="book-pull")
    #path("", pull_books, name="book-pull")
]

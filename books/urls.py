from django.urls import path
from books.views import BookListApiView, BookApiView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('books/<int:pk>', BookApiView.as_view(), name='book-api-view'),
    path('books/', BookListApiView.as_view(), name='book-list-api-view'),
]
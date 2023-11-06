from django.urls import path
from db.views import pull_books

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', pull_books, name='book-pull')
]
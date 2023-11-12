from django.urls import path
from db.views import PullBooksApiView

urlpatterns = [
    path("", PullBooksApiView.as_view(), name="book-pull"),

]

#add some code

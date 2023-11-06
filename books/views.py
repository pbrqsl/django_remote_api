from django.shortcuts import render
from rest_framework.viewsets import generics
from books.serializers import BookSerializer
from books.models import Book


class BookListApiView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        if len(self.request.GET) > 0:
            query_set = {}
            for query in self.request.GET:
                print(query)
                query_set[query] = self.request.GET.get(query)
        print(self.request.GET)
            
        return super().get_queryset()
    

class BookApiView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    many = True


# Create your views here.

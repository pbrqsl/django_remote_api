from rest_framework.viewsets import generics
from books.serializers import BookSerializer
from books.models import Book
from django.db.models import Q
from functools import reduce
import operator


class BookListApiView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        result = super().get_queryset()
        if len(self.request.GET) == 0:
            return result
        
        query_params = {}
        for item in self.request.GET.lists():
            if item[0].lower() == "author":
                query_params["authors"] = item[1]
            elif item[0].lower() == "category":
                query_params["categories"] = item[1]
        for query in self.request.GET:
            query_params[query.lower()] = self.request.GET.get(query)

        book_fields = [x.attname for x in Book._meta.get_fields()]

        for param in query_params:
            if param == "sort":
                result = result.order_by(query_params[param])
            elif param == "authors":
                query = reduce(
                    operator.or_,
                    (Q(authors__icontains=x) for x in query_params[param]),
                )
                result = result.filter(query)
            elif param == "categories":
                query = reduce(
                    operator.or_,
                    (Q(categories__icontains=x) for x in query_params[param]),
                )

                result = result.filter(query)

            elif param in book_fields:
                query_params[param] = query_params[param].lstrip('"').rstrip('"')
                result = result.filter(**{param: query_params[param]})
        return result


class BookApiView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    many = True


# Create your views here.

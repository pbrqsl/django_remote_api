from django.shortcuts import render
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from books.serializers import BookSerializer
from books.models import Book
from db.serializers import BookToDbSerializer
import json


@api_view(["POST"])
def pull_books_with_serializer(request):
    URL = "https://www.googleapis.com/books/v1/volumes"

    body = json.loads(request.body.decode("utf-8"))
    params = dict(q=body["q"])
    response = requests.get(url=URL, params=params)
    books = response.json()["items"]
    serialized_books_out = BookToDbSerializer(books, many=True)
    serialized_books_in = BookSerializer(data=serialized_books_out.data, many=True)
    print(serialized_books_in.is_valid())

    serialized_books_in.save()
    
    return Response({"message": "books_indexed"})


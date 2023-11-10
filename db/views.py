from django.shortcuts import render
from rest_framework.response import Response
import requests
from rest_framework.decorators import api_view
from books.serializers import BookSerializer
from books.models import Book
from db.serializers import BookToDbSerializer
import json


@api_view(["POST"])
def pull_books(request):
    URL = "https://www.googleapis.com/books/v1/volumes"

    body = json.loads(request.body.decode("utf-8"))
    params = dict(q=body["q"])
    response = requests.get(url=URL, params=params)
    books = response.json()
    for book in books["items"]:
        title = book["volumeInfo"]["title"]
        authors = book["volumeInfo"].get("authors")
        categories = book["volumeInfo"].get("categories")
        published_date = book["volumeInfo"].get("publishedDate")
        # thumbnail = book['volumeInfo']['imageLinks'].get('thumbnail')
        thumbnail = book["volumeInfo"].get("imageLinks", {}).get("thumbnail")
        average_rating = book["volumeInfo"].get("averageRating")
        ratings_count = book["volumeInfo"].get("ratingsCount")

        #print(Book.objects.filter(title=title))

        if not Book.objects.filter(title=title):
            print("---------ADDING BOOK-------------")
            new_book = Book(
                title=title,
                authors=authors,
                published_date=published_date,
                categories=categories,
                thumbnail=thumbnail,
                average_rating=average_rating,
                ratings_count=ratings_count,
            )
            new_book.save()

        # authors = book['volumeInfo']['authors']
        # print(title)
        # print(authors)
        # new_book = Book(title = title)
        # print(new_book.title)
        # new_book.save()

    return Response({"message": "books_indexed"})

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

# Create your views here.

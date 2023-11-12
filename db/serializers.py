from rest_framework import serializers
from books.models import Book



class BookToDbSerializer(serializers.Serializer):
    title = serializers.CharField(source='volumeInfo.title')
    authors = serializers.ListField(source='volumeInfo.authors', required=False)
    published_date = serializers.DateField(source='volumeInfo.publishedDate', required=False)
    categories = serializers.ListField(source='volumeInfo.categories', required=False)
    thumbnail = serializers.CharField(source='volumeInfo.imageLinks.thumbnail', required=False)
    average_rating = serializers.CharField(source='volumeInfo.averageRating', required=False)
    rating_count = serializers.CharField(source='volumeInfo.ratingCount', required=False)

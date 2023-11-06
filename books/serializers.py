from rest_framework import serializers
from books.models import Book
from collections import OrderedDict


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret_no_null = OrderedDict()
        for item in ret:
            if ret[item]:
                ret_no_null[item] = ret[item]
        return ret_no_null
from rest_framework import serializers
from .models import *

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=BookCategory
        fields='__all__'

class BorrowingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Borrowing
        fields='__all__'       
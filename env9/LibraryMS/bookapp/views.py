from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serialisers import *

# Create your views here.

class ListbookCategory(generics.ListCreateAPIView):
    queryset= BookCategory.objects.all()
    serializer_class= BookCategorySerializer 

class DetailsbookCategory(generics.RetrieveUpdateDestroyAPIView):
    queryset= BookCategory.objects.all()
    serializer_class= BookCategorySerializer 

class ListBorrow(generics.ListCreateAPIView):
    queryset= Borrowing.objects.all()
    serializer_class= BorrowingSerializer

class DetailsBorrow(generics.RetrieveUpdateDestroyAPIView):
    queryset= Borrowing.objects.all()
    serializer_class= BorrowingSerializer     
from django.shortcuts import render
from .models import *
from .serializers import*
from .permissions import*
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ListUserCustom(generics.ListCreateAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerialisers 
    permission_classes=[IsUserOrReadOnly]

class DetailsUserCustom(generics.RetrieveUpdateDestroyAPIView):
    queryset= CustomUser.objects.all()
    serializer_class= UserSerialisers
    permission_classes=[IsUserOrReadOnly]
from django.urls import path
from .views import *


urlpatterns=[
path('listbook/',ListbookCategory.as_view(), name='listbook'),
path('detailbook/<int:pk>',DetailsbookCategory.as_view(), name='detailbook'),
path('listbookborrowed/',ListBorrow.as_view(), name='listbookborrowed'),
path('detailbookborrowed/<int:pk>',DetailsBorrow.as_view(), name='detailbookborrowed'),
]
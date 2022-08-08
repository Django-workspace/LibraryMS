from django.urls import path
from .views import *


urlpatterns=[
path('listUser/',ListUserCustom.as_view(), name='listuser'),
path('detailUser/<int:pk>',ListUserCustom.as_view(), name='detailuser'),
]
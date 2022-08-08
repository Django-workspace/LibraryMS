from rest_framework import serializers
from .models import*


class UserSerialisers(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields='__all__'
from rest_framework import serializers
from .models import Books


# εΊεεε¨
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

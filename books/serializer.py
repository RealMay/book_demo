from rest_framework import serializers
from .models import Books


# 序列化器
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

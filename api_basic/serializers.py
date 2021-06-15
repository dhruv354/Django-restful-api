from .models import Article
from rest_framework import serializers
from django.db import models

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=35)
    author = serializers.CharField(max_length=35)
    email = serializers.EmailField(max_length=20)
    date = serializers.DateField()

    def create(self, validated_data):
        return Article.objects.create(validated_data)



    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.email = validated_data.get('email', instance.email)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

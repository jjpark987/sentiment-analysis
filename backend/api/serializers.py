from rest_framework import serializers
from django.contrib.auth.models import User
from .models import SearchQuery, Product, Review, Analysis

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class SearchQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchQuery
        fields = ['id', 'query', 'created_at', 'user']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'latest_price', 'seller', 'description', 'url', 'created_at', 'updated_at', 'favorited_by']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'rating', 'content', 'location', 'date', 'helpfulness', 'created_at', 'product']

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['id', 'title', 'response', 'created_at', 'user', 'product', 'reviews']
        
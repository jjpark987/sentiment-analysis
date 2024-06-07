from rest_framework import serializers
from .models import Product, Review

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'image_url', 'latest_price', 'seller', 'description', 'url', 'created_at', 'updated_at', 'favorited_by']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'rating', 'content', 'location', 'date', 'helpfulness', 'created_at', 'product']
        
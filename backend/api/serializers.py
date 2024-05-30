from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Analysis

class UserSerializer(serializers.ModelSerializer):
    # defines the fields to be included in the serializer
    class Meta:
        # specifies django model for this serializer
        model = User
        # lists the fields to be serialized
        fields = ['id', 'username', 'password']
        # specifies additional options for specific fields
        # {'write_only': True} means the password field won't be returned in the response
        extra_kwargs = {
            'password': {'write_only': True},
        }

    # called by the view to create new user
    def create(self, validated_data):
        # creates new user instance using validated data
        # **validated_data unpacks dictionary as keyword arguments
        user = User.objects.create_user(**validated_data)
        return user
    
class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['id', 'title', 'response', 'created_at', 'user', 'product', 'reviews']
        extra_kwargs = {
            'user': {'read_only': True},
            'product': {'read_only': True},
            'reviews': {'read_only': True},
        }
        
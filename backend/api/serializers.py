from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        # 'write_only': True means no one read the password
        extra_kwargs = {'password': {'write_only': True}}

    # validated_data is data that has validated the model and its fields
    def create(self, validated_data):
        # creates a new user using the validated data
        # ** splits the keyword arguements from a dictionary
        user = User.objects.create_user(**validated_data)
        return user
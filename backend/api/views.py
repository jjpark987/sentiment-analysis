from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CreateUserView(generics.CreateAPIView):
    # gets all the User objects, so we don't create duplicates
    queryset = User.objects.all()
    # serializer tells views what kind of data we accept to create new User
    serializer_class = UserSerializer
    # anyone can create a new user
    permission_classes = [AllowAny]
import asyncio
from asgiref.sync import async_to_sync
from web_scraper.playwright import test_async_method
from rest_framework import viewsets, permissions
from rest_framework_simplejwt import views, authentication
from .models import User, Analysis
from .serializers import UserSerializer, AnalysisSerializer

# custom view that initiates playwright on successful login
class CustomTokenObtainPairView(views.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        print('Starting custom post view')
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            asyncio.run(test_async_method())
        return response
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [authentication.JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return User.objects.all()
        return User.objects.filter(user=user)

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

class AnalysisViewSet(viewsets.ModelViewSet):
    serializer_class = AnalysisSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    allowed_actions = ['list', 'retrieve', 'create', 'destroy']

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Analysis.objects.all()
        return Analysis.objects.filter(user=user)
    
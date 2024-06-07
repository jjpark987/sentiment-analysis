from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from .models import User, Analysis
from .serializers import UserSerializer, AnalysisSerializer

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
    
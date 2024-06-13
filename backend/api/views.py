from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from .models import User, SearchQuery, Product, Review, Analysis
from .serializers import UserSerializer, SearchQuerySerializer, ProductSerializer, ReviewSerializer, AnalysisSerializer
    
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
    
class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.JWTAuthentication]
    allowed_actions = ['list', 'retrieve', 'create', 'destroy']

    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class SearchQueryViewSet(BaseViewSet):
    serializer_class = SearchQuerySerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return SearchQuery.objects.all()
        return SearchQuery.objects.filter(user=user)

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(BaseViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class AnalysisViewSet(BaseViewSet):
    serializer_class = AnalysisSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Analysis.objects.all()
        return Analysis.objects.filter(user=user)
    
from rest_framework import views, viewsets, permissions
from rest_framework_simplejwt import authentication
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer

class BaseViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.JWTAuthentication]
    allowed_actions = ['list', 'retrieve', 'create', 'destroy']

    def get_permissions(self):
        if self.action == 'destroy':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

class ProductViewSet(BaseViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ReviewViewSet(BaseViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ProductSearchView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

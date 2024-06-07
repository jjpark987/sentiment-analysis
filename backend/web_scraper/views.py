from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
# from django.views.decorators.csrf import csrf_exempt

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

# @csrf_exempt
# async def get_search_query(request):
#     # retrieves the value of the query parameter 'search' from request URL
#     # default is ''
#     search_query = request.GET.get('search', '')

#     return JsonResponse({'search_query': search_query})
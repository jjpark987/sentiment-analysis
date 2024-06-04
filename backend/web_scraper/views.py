from rest_framework import viewsets, permissions
from rest_framework_simplejwt import authentication
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from django.views.decorators.csrf import csrf_exempt

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    allowed_actions = ['list', 'retrieve', 'create', 'destroy']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    allowed_actions = ['list', 'retrieve', 'create', 'destroy']

# @csrf_exempt
# async def get_search_query(request):
#     # retrieves the value of the query parameter 'search' from request URL
#     # default is ''
#     search_query = request.GET.get('search', '')

#     return JsonResponse({'search_query': search_query})
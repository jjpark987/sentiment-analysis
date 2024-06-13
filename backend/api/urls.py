from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserViewSet, SearchQueryViewSet, ProductViewSet, ReviewViewSet, AnalysisViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'search-queries', SearchQueryViewSet, basename='search-query')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'analyses', AnalysisViewSet, basename='analysis')

urlpatterns = [    
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='get_token'),    # POST
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),  # POST
]

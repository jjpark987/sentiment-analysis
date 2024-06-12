from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomTokenObtainPairView, UserViewSet, AnalysisViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'analyses', AnalysisViewSet, basename='analysis')

urlpatterns = [    
    path('', include(router.urls)),
    # jwt token based authentication
    path('token/', CustomTokenObtainPairView.as_view(), name='get_token'),    # POST
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),  # POST
]

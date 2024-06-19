from django.urls import path
from .views import ScraperTaskView

urlpatterns = [
    path('initialize/', ScraperTaskView.as_view(), name='initialize'),
]

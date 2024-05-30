from django.db import models
from django.contrib.auth.models import User
from web_scraper.models import Product, Review
    
class Analysis(models.Model):
    title = models.CharField(max_length=200)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='analyses')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='analyses')
    reviews = models.ManyToManyField(Review, related_name='reviews')
    
    def __str__(self) -> str:
        return self.title
    
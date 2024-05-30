from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.URLField()
    latest_price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    favorited_by = models.ManyToManyField(User, related_name='favorite_products', blank=True)

    def __str__(self) -> str:
        return self.name
    
class Review(models.Model):
    title = models.CharField(max_length=200)
    rating = models.IntegerField()
    content = models.TextField()
    location = models.CharField(max_length=50)
    date = models.DateField()
    helpfulness = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    
    def __str__(self) -> str:
        return self.title
    
from django.db import models
from django.contrib.auth.models import User
from web_scraper.models import Product
    
class Analysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='analyses')
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name='analyses')
    
    title = models.CharField(max_length=200)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
from django.contrib import admin
from .models import SearchQuery, Product, Review, Analysis

admin.site.register(SearchQuery)
admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Analysis)
from django.contrib import admin
from .models import Brand, Product, Rating, Category, Review

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Review)

import random
from statistics import mean

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render, redirect

from .models import Product, Review, Rating, Category
from .helpers.stars import get_ratings_context

class HomeView(View):
	def get(self, request):
		categories = Category.objects.order_by('name').all().values_list('name')[:10]
		categories = [category[0] for category in categories]

		products = Product.objects.all()[:6]
		products = [{'id': product.id, 
					 'name': product.name, 
					 'price': product.price,
					 'description': product.description,
					 'ratings': get_ratings_context(Rating.objects.filter(product=product.id).values_list('rating'))
					 } for product in products]
		context = {
			'products': products,
			'categories': categories
		}

		return render(request, 'index.html', context)


class RedirectView(View):
	def get(self, request):
		return redirect('shop/')

class ProductView(View):
	def get(self, request, **kwargs):
		id_collection = Product.objects.values_list('id')
		pid = kwargs['pid']
		product = Product.objects.get(pk=pid)
		related_products = [{'id': related.id, 
							 'name': related.name,
							 'price': related.price
							 } for related in product.related_products.all()[:3]]
		reviews = Review.objects.filter(product=pid)

		ratings = Rating.objects.filter(product=pid).values_list('rating')
		ratings_context = get_ratings_context(ratings)

		context = {
			'id': product.id,
			'name': product.name,
			'description': product.description,
			'price': product.price,
			'related_products': related_products,
			'reviews': reviews,
			'ratings': ratings_context
		}

		return render(request, 'product.html', context)

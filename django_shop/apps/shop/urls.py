from django.urls import path
from .views import HomeView, ProductView

urlpatterns = [
	path('', HomeView.as_view()),
	path('products/<int:pid>/', ProductView.as_view()),
]
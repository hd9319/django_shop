from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include

from .apps.shop.views import RedirectView

urlpatterns = [
    path('', RedirectView.as_view()),
    path('admin/', admin.site.urls),
    path('shop/', include('django_shop.apps.shop.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

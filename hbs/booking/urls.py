from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('booking_create', views.booking_create, name='booking_create'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
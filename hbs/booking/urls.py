from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('booking_create', views.booking_create, name='booking_create'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donate, name='donate'),
    path('callback/', views.mpesa_callback, name='mpesa_callback'),
]
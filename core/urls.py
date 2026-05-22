from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('healing/', views.healing, name='healing'),
    path('healing/callback/', views.healing_callback, name='healing_callback'),
]
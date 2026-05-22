from django.urls import path
from . import views

urlpatterns = [
    path('', views.say_names, name='say_names'),
    path('received/', views.submission_received, name='submission_received'),
]
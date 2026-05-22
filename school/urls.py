from django.urls import path
from . import views

urlpatterns = [
    path('', views.school, name='school'),
    path('your-rights/', views.your_rights, name='your_rights'),
    path('constitution/', views.constitution, name='constitution'),
    path('philosophy/', views.philosophy, name='philosophy'),
]
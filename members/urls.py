from django.urls import path
from . import views

urlpatterns = [
    path('', views.join, name='join'),
    path('callback/', views.join_callback, name='join_callback'),
    path('check/<uuid:member_id>/', views.check_payment, name='check_payment'),
    path('success/<uuid:member_id>/', views.success, name='join_success'),
]
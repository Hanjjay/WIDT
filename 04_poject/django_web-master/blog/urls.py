from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('method/', views.method, name='method'),
    path('result/', views.result, name='result'),
    path('conclusion/', views.conclusion, name='conclusion'),
]
from django.urls import path
from . import views

app_name = 'q3'

urlpatterns = [
    path('calculate/', views.calculate, name='calculate'),
    path('result/', views.result, name='result'),
]

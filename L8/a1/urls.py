from django.urls import path
from . import views

app_name = 'a1'

urlpatterns = [
    path('bill/', views.bill, name='bill'),
    path('result/', views.result, name='result'),
]

from django.urls import path
from . import views

app_name = 'a2'

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('thank-you/', views.thank_you, name='thank_you'),
]

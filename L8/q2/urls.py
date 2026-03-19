from django.urls import path
from . import views

app_name = 'q2'

urlpatterns = [
    path('vote/', views.vote, name='vote'),
    path('results/', views.results, name='results'),
]

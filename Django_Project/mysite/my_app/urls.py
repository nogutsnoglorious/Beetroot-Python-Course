from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('child/', views.return_simple_html, name='child'),
    path('football/', views.football, name='football'),
    path('most/', views.most_expensive_artworks, name='most'),
    path('fitness/', views.fitness, name='fitness')
]
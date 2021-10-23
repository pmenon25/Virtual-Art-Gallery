from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('info/', views.info, name='info'),
    path('artists/', views.artist, name='artist'),
    path('exhibition/create/' , views.create_exhibition)
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('info/', views.info, name='info'),
    path('artists/', views.artist, name='artist'),
    path('exhibition/' , views.exhibition),
    path('exhibition/new/', views.new),
    path('exhibition/submit/' , views.create_exhibition),
    path('accounts/signup/', views.signup, name='signup'),
]

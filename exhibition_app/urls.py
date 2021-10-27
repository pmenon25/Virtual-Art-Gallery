from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('info/', views.info, name='info'),
    path('artists/', views.artist, name='artist'),
    # exhibition
    path('exhibition/' , views.exhibition, name='exhibitions'),
    path('exhibition/<int:exhibition_id>/' , views.details_exhibition, name='details'),
    path('exhibition/new/', views.new, name='newexhibition'),
    path('exhibition/submit/' , views.create_exhibition),
    path('exhibition/<int:exhibition_id>/delete/' , views.delete_exhibition),
    path('exhibition/<int:exhibition_id>/edit/' , views.edit_exhibition),
    path('exhibition/<int:exhibition_id>/update/' , views.update_exhibition),
    # art
    path('exhibition/<int:exhibition_id>/add_art/', views.add_art, name='add_art'),
    path('exhibition/<int:art_id>/delete_art/' , views.delete_art),
    path('exhibition/<int:art_id>/edit_art/' , views.edit_art),
    path('exhibition/<int:art_id>/update_art/' , views.update_art),
    path('accounts/signup/', views.signup, name='signup'),
]

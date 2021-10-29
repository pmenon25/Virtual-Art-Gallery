from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.info, name='about'),
    path('artists/', views.artist, name='artist'),
    path('artists/<int:exhibition_id>/profile/' , views.profile),
    # exhibition
    path('exhibition/' , views.exhibition, name='exhibitions'),
    path('exhibition/<int:exhibition_id>/' , views.details_exhibition, name='details'),
    path('exhibition/new/', views.new, name='newexhibition'),
    path('exhibition/submit/' , views.create_exhibition),
    path('exhibition/<int:exhibition_id>/delete/' , views.delete_exhibition),
    path('exhibition/<int:exhibition_id>/edit/' , views.edit_exhibition),
    path('exhibition/<int:exhibition_id>/update/' , views.update_exhibition),
    
    # art
   path('exhibition/<int:exhibition_id>/add_art/', views.add_art, name = 'add_art'),
    path('exhibition/<int:art_id>/delete_art/' , views.delete_art),
    path('exhibition/<int:art_id>/edit_art/' , views.edit_art),
    path('exhibition/<int:art_id>/update_art/' , views.update_art),
    path('accounts/signup/', views.signup, name='signup'),

    
    #comment
    path('artists/<int:exhibition_id>/add_comment/', views.add_comment, name='add_comment'),
    path('artists/<int:comment_id>/delete_comment/' , views.delete_comment),
    path('artists/<int:comment_id>/edit_comment/' , views.edit_comment),
    path('artists/<int:comment_id>/update_comment/' , views.update_comment),
    

    #like
    path('exhibition/<int:exhibition_id>/add_like/', views.add_like, name='add_like')
    
]   

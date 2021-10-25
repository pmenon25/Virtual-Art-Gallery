from django.db import models
from datetime import date
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Exhibition(models.Model):
    title = models.CharField(max_length = 100)
    artist_name = models.CharField(max_length= 100)
    description = models.CharField(max_length=250)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.title} on {self.artist_name} and {self.date}'

class Art(models.Model):
    name = models.CharField(max_length= 100)
    description = models.CharField(max_length= 250)
    exhibition = models.ForeignKey(Exhibition , on_delete=models.CASCADE)
    art_img = models.ImageField(upload_to='images/')
    #uploard to will specify which dir the images should reside 

    def __str__(self) :
        return f'{self.name} on {self.description} and {self.exhibition}'

class Comment(models.Model):
    comment = models.CharField(max_length=250)
    exhibition = models.ForeignKey(Exhibition , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}on {self.exhibition}'

class Likes (models.Model):
    likes = models.IntegerField()
    exhibition = models.ForeignKey(Exhibition , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.likes}on {self.exhibition}'

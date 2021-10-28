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

    def __str__(self) :
        return f'{self.name} on {self.description} and {self.exhibition}'

class Comment(models.Model): #add datefield
    name = models.CharField(max_length=80, default='name')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    exhibition = models.ForeignKey(Exhibition , on_delete=models.CASCADE)
     


    class Meta: 
        ordering = ['created',] 

    def __str__(self):
        return f'{self.name}on {self.comment} and {self.exhibition}'

class Like (models.Model):
    likes = models.IntegerField(default=0)
    exhibition = models.ForeignKey(Exhibition , on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.likes}on {self.exhibition}'

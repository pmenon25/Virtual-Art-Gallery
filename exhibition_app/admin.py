from django.contrib import admin
from .models import Comment, Exhibition, Like

# Register your models here.
admin.site.register(Comment)
admin.site.register(Exhibition)
admin.site.register(Like)


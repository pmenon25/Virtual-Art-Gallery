from django.contrib import admin
from .models import Comment, Exhibition, Art

# Register your models here.
admin.site.register(Comment)
admin.site.register(Exhibition)
# admin.site.register(Like)
admin.site.register(Art)

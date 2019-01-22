from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'status', 'created_at', 'updated_at']

#admin.site.register(Post, PostAdmin)

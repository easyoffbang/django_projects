from django.contrib import admin
from .models import Post
from django.utils.safestring import mark_safe
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content_size', 'created_at', 'updated_at']

    def content_size(self, post):
        return mark_safe('<strong>{}글자</strong>'.format(len(post.content)))
    content_size.short_description = '글자수'

admin.site.register(Post, PostAdmin)

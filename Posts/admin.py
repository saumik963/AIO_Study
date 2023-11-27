from django.contrib import admin
from .models import Post, PostImages

class PostImagesAdmin(admin.StackedInline):
    model = PostImages

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'PostTitle', 'Description', 'is_post', 'update_at']
    fields = ['user', 'PostTitle', 'Description', 'is_post', 'Coverimage', 'created_at', 'update_at']
    readonly_fields = ['created_at', 'update_at']
    inlines = [PostImagesAdmin]  # Add PostImagesAdmin as an inline

@admin.register(PostImages)
class PostImagesAdmin(admin.ModelAdmin):
    pass

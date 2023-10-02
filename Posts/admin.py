from django.contrib import admin
from .models import Post


@admin.register(Post)
class NotesAdmin(admin.ModelAdmin):
    list_display = ['user', 'PostTitle',
                    'Description', 'is_post', 'update_at']
    fields = ['user', 'PostTitle',
              'Description', 'is_post', 'image', 'created_at', 'update_at']
    readonly_fields = ['created_at', 'update_at']
    # search_fields = ('user', 'PostTitle', 'Description')

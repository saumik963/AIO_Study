from django.contrib import admin
<<<<<<< HEAD
from .models import Post, PostImages,Comments
=======
from .models import Post, PostImages
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47

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
<<<<<<< HEAD

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display=['user','post','review','created_at']
=======
>>>>>>> d66e195d0d0125032295095ecbc08a3042446d47

from django.urls import path, include
from . import views
urlpatterns = [
    path('Post/', views.User_post, name='Post'),
    path('Posts/', views.View_posts, name='Posts'),
    path('post_detail/<int:id>/', views.post_detail, name='post_detail'),
    path('public/<int:id>/', views.public, name='public'),
    path('DeletePost/<int:id>/', views.DeletePost, name='DeletePost'),
    path('edit_post/<int:id>/', views.edit_post, name='edit_post'),
]

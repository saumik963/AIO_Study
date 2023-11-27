from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    PostTitle = models.CharField(max_length=100)
    Description = models.CharField(max_length=10000)

    Coverimage = models.ImageField(blank=True, upload_to='CoverPhotos')

    is_post = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.PostTitle} - {self.user}"

class PostImages(models.Model):
    post=models.ForeignKey(Post,default=None,on_delete=models.CASCADE)
    images=models.ImageField(upload_to='PostImages')

    def __str__(self) :
        return self.post.PostTitle